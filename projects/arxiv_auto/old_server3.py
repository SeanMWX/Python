import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from mysql.connector import Error
from urllib.parse import urlparse

def get_config():
    """读取配置"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_db_connection():
    """创建数据库连接"""
    config = get_config()
    db_config = {
        'host': config['database']['host'],
        'user': config['database']['user'],
        'password': config['database']['password'],
        'database': config['database']['database']
    }
    return mysql.connector.connect(**db_config)

def fetch_articles_from_table(table_name):
    """根据表名从数据库中获取最新一天的文章数据"""
    articles_data = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT MAX(updated) FROM {table_name}
        """)
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
    except Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return articles_data

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # 解析请求路径
        path = urlparse(self.path).path
        
        # 根据路径选择表名
        if path == "/":
            table_name = "arxiv_daily"
            self.send_response(200)
        elif path == "/ai":
            table_name = "arxiv_daily"  # 用于AI数据的表名
            self.send_response(200)
        elif path == "/sc":
            table_name = "security_table"  # 用于Security数据的表名
            self.send_response(200)
        else:
            self.send_error(404, "File Not Found")
            return

        articles = fetch_articles_from_table(table_name)

        # 开始构建HTML响应
        self.send_header("Content-type", "text/html")
        self.end_headers()

        
        # 将所有部分组合起来并发送响应
        full_html = generate_html(articles, path)
        self.wfile.write(full_html.encode("utf-8"))

def generate_html(articles, path):
    html_header = generate_html_header(articles, path)
    html_content = generate_html_content(articles)
    html_footer = generate_html_footer()
    return html_header + html_content + html_footer

def generate_html_header(articles, path):

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
    if path == "/":
        html_header += """
    _              _                         _    ___ 
   / \   _ ____  _(_)_   ___    ___ ___     / \  |_ _|
  / _ \ | '__\ \/ / \ \ / (_)  / __/ __|   / _ \  | | 
 / ___ \| |   >  <| |\ V / _  | (__\__ \_ / ___ \ | | 
/_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)_/   \_\___|
    </pre>
        <h1>Arxiv: cs.AI</h1>
"""
    elif path == "/ai":
        html_header += """
    _              _                         _    ___ 
   / \   _ ____  _(_)_   ___    ___ ___     / \  |_ _|
  / _ \ | '__\ \/ / \ \ / (_)  / __/ __|   / _ \  | | 
 / ___ \| |   >  <| |\ V / _  | (__\__ \_ / ___ \ | | 
/_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)_/   \_\___|
    </pre>
        <h1>Arxiv: cs.AI</h1>
"""
    elif path == "/sc":
        html_header += """<h1>Arxiv: Security</h1>"""

    html_header += f"""
        <p>今日文章总数: {len(articles)}</p>
        <p>更新时间: {articles[0][-3] if articles else 'N/A'} (+00:00)</p>
    </div>
"""
    return html_header

def generate_html_content(articles):
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

def generate_html_footer():
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

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    config = get_config()
    port = int(config['server'].get('port', 80))  # 获取端口配置，未配置则默认为80
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()