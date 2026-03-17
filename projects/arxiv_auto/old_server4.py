import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from mysql.connector import Error
from urllib.parse import urlparse

# 配置管理
class Config:
    def __init__(self, filename='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def db_config(self):
        return self.config['database']

    def server_port(self):
        return int(self.config['server'].get('port', 80))

# 数据库操作
class Database:
    def __init__(self, db_config):
        self.db_config = db_config

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def fetch_articles_from_table(self, table_name):
        articles_data = []
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT MAX(updated) FROM {table_name}")
            result = cursor.fetchone()
            latest_date = result[0] if result else None
            
            if latest_date:
                cursor.execute(f"""
                    SELECT title, summary, authors, categories, comment, entry_id, journal_ref, updated, CN_title, CN_summary
                    FROM {table_name}
                    WHERE DATE(updated) = DATE(%s)
                    ORDER BY updated DESC
                """, (latest_date,))
                articles_data = cursor.fetchall()
        return articles_data
    
    def get_latest_article_date_and_count(self, table_name):
        """获取指定表中最新文章的更新日期和当天更新的文章数量"""
        latest_date = None
        count = 0
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # 查询最新更新日期
            cursor.execute(f"SELECT MAX(DATE(updated)) FROM {table_name}")
            result = cursor.fetchone()
            if result and result[0]:
                latest_date = result[0]
                
                # 基于最新更新日期，查询当天更新的文章数量
                cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE DATE(updated) = %s", (latest_date,))
                count_result = cursor.fetchone()
                if count_result:
                    count = count_result[0]
                    
        return latest_date, count

# HTTP请求处理器
class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.config = Config()
        self.db = Database(self.config.db_config())
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path.strip('/')
        if path not in ('', 'ai', 'cr'):
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.generate_404_html().encode("utf-8"))
            return
        
        if path == "":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.generate_index_html().encode("utf-8"))
            return

        table_mapping = {'ai': 'arxiv_cs_ai', 'cr': 'arxiv_cs_cr'}
        
        table_name = table_mapping.get(path, 'arxiv_cs_ai')
        articles = self.db.fetch_articles_from_table(table_name)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(self.generate_html(articles, path).encode("utf-8"))

    def generate_html(self, articles, path):
        html_header = self.generate_html_header(articles, path)
        html_content = self.generate_html_content(articles)
        html_footer = self.generate_html_footer()
        return html_header + html_content + html_footer

    def generate_html_header(self, articles, path):

        # Header
        html_header = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Arxiv: cs.AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            /* 基础重置 */
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                background-color: #f0f0f2; /* 微妙的灰色背景 */
                color: #333; /* 深灰色文字，增加对比度但不过分强烈 */
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* 更现代的字体 */
            }

            /* 主内容区 */
            .content {
                display: flex;
                justify-content: center;
                text-align: left;
                padding: 20px;
                min-height: calc(100vh - 60px);
                line-height: 1.5;
            }

            /* 内部容器 */
            .inner-content {
                max-width: 1200px;
                width: 100%;
                background: #fff; /* 白色背景提升内容可读性 */
                box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* 微妙的阴影增加立体感 */
                padding: 20px; /* 内容与边缘的距离 */
                border-radius: 5px; /* 轻微的圆角 */
            }

            /* 页脚样式 */
            .site-info {
                background-color: #f1f1f1; /* 页脚背景色 */
                color: #333; /* 页脚文字色 */
                text-align: center;
                padding: 10px 0;
                font-size: 14px;
            }

            /* 链接样式 */
            a {
                color: #007bff;
                text-decoration: none;
                transition: color 0.3s ease-in-out;
            }

            a:hover, a:focus {
                color: #0056b3;
                text-decoration: underline;
            }

            /* 文章容器样式 */
            .article-container {
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
                border-bottom: 1px solid #e0e0e0;
                padding-bottom: 15px;
            }

            /* 文章左侧和右侧样式 */
            .article-left, .article-right {
                width: 48%;
            }

            /* 文章标题和摘要样式 */
            .article-title, .article-summary {
                margin: 5px 0;
            }

            /* 增加科技感的标题样式 */
            h1 {
                color: #333;
                text-align: center;
                font-weight: 300;
                letter-spacing: -1px; /* 字母间距调整 */
            }

            /* 微调滚动条样式 */
            ::-webkit-scrollbar {
                width: 8px;
            }

            ::-webkit-scrollbar-track {
                background: #f1f1f1;
            }

            ::-webkit-scrollbar-thumb {
                background: #888;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #555;
            }

            .header-info {
                text-align: center;
                padding: 20px;
                background-color: #eef;
                border-bottom: 1px solid #ddd;
            }

            .header-info h1 {
                margin: 0 0 10px 0;
            }

            .header-info p {
                margin: 5px 0;
                color: #666;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
    <div class="header-info">
        <pre>
    """
        if path == "ai":
            html_header += """
    _              _                         _    ___ 
   / \   _ ____  _(_)_   ___    ___ ___     / \  |_ _|
  / _ \ | '__\ \/ / \ \ / (_)  / __/ __|   / _ \  | | 
 / ___ \| |   >  <| |\ V / _  | (__\__ \_ / ___ \ | | 
/_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)_/   \_\___|
        </pre>
            <h1>Arxiv: cs.AI</h1>
    """
        elif path == "cr":
            html_header += """
    _              _                      ____ ____  
   / \   _ ____  _(_)_   ___    ___ ___  / ___|  _ \ 
  / _ \ | '__\ \/ / \ \ / (_)  / __/ __|| |   | |_) |
 / ___ \| |   >  <| |\ V / _  | (__\__ \| |___|  _ < 
/_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)____|_| \_\\
        </pre>
            <h1>Arxiv: cs.CR</h1>
    """

        html_header += f"""
            <p>Articles: {len(articles)}</p>
            <p>Last Updated: {articles[0][-3] if articles else 'N/A'} (+00:00)</p>
        </div>
    """
        return html_header

    def generate_html_content(self, articles):
        # 初始化文章内容HTML字符串
        html_content = ""
        html_content = """
    <div class="content">
        <div class="inner-content">        
    """

            # 遍历所有文章，将它们添加到HTML中
        for article in articles:
            title, summary, authors, categories, comment, entry_id, journal_ref, updated, CN_title, CN_summary = article
            html_content += "<div class=\"article-container\">"
            # 英文内容（左侧）
            html_content += f"<div class=\"article-left\"><h3 class=\"article-title\">Title: {title}</h3><p class=\"article-summary\">Summary: {summary}</p><p><i>Updated: {updated}</i></p></div>"
            # 中文内容（右侧）
            html_content += f"""
            <div class=\"article-right\"><h3 class=\"article-title\">标题: {CN_title}</h3><p class=\"article-summary\">摘要: {CN_summary}</p>
            <p><i>更新时间: {updated}</i></p>
            <p><i>领域: {categories}</i></p>
            <p><i>下载: <a href="{entry_id}" target="_blank">{entry_id}</a></i></p>
            </div>
            """
            html_content += "</div>"

        html_content += """
        </div>
    </div>
    """
        return html_content

    def generate_html_footer(self):
        # HTML页面的结尾部分
        html_footer = """
    <div class="site-info">
        Xinhai (Sean) Zou 粤ICP备20040781号. <br/>
        This website does not contain any JavaScript code. <br/>
    </div>

    </body>
    </html>
    """
        return html_footer
    
    def generate_404_html(self):
        """生成404错误页面的HTML"""
        return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>404 Not Found</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            background-color: #f0f0f2;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .content {{
            display: flex;
            justify-content: center;
            text-align: center;
            padding: 20px;
            min-height: calc(100vh - 60px);
            line-height: 1.5;
        }}
        .inner-content {{
            max-width: 1200px;
            width: 100%;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            border-radius: 5px;
        }}
        .site-info {{
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="content">
        <div class="inner-content">
            <h1>404 Not Found</h1>
            <p>The resource you are looking for could not be found.</p>
        </div>
    </div>
    <div class="site-info">
        Xinhai (Sean) Zou 粤ICP备20040781号. <br/>
        This website does not contain any JavaScript code. <br/>
    </div>
</body>
</html>
        """
    
    def generate_index_html(self):
        # 获取arxiv_cs_ai和arxiv_cs_cr表的最新更新日期和当天文章更新数目
        latest_ai_date, ai_count = self.db.get_latest_article_date_and_count("arxiv_cs_ai")
        latest_cr_date, cr_count = self.db.get_latest_article_date_and_count("arxiv_cs_cr")
        
        latest_ai_date = latest_ai_date.strftime('%Y-%m-%d') if latest_ai_date else 'N/A'
        latest_cr_date = latest_cr_date.strftime('%Y-%m-%d') if latest_cr_date else 'N/A'

        return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Arxiv Index</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            background-color: #f0f0f2;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 20px;
            min-height: calc(100vh - 60px);
            line-height: 1.5;
        }}
        .inner-content {{
            max-width: 1200px;
            width: 100%;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .site-info {{
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
            transition: color 0.3s ease-in-out;
        }}
        a:hover, a:focus {{
            color: #0056b3;
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="content">
        <h1>Welcome to Arxiv Day</h1>
        <div class="inner-content">
            <h2>We collect:</h2>
            <p><a href="/ai">Arxiv: cs.AI</a> - Latest Update: {latest_ai_date}, Articles: {ai_count}</p>
            <p><a href="/cr">Arxiv: cs.CR</a> - Latest Update: {latest_cr_date}, Articles: {cr_count}</p>
        </div>
        <div class="inner-content">
            <h2>What is Arxiv Day?</h2>
            <p>We are collecting all YESTERDAY's arxiv papers, and translate them to Chinese. Future may have API and more abilities.</p>
            <p>Source code will be released in <a href="https://github.com/SeanMWX/ArxivDay">Github</a> in few days.</p>
        </div>
        <div class="inner-content">
            <h2>Contact me.</h2>
            <p><a href="https://seanzou.com">Sean Zou</a></p>
        </div>
    </div>
    <div class="site-info">
        Xinhai (Sean) Zou 粤ICP备20040781号. <br/>
        This website does not contain any JavaScript code. <br/>
    </div>
</body>
</html>
        """

def run():
    config = Config()
    port = config.server_port()
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()