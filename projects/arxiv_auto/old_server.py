from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 连接到数据库
        try: 
            conn = mysql.connector.connect(
                host="localhost",
                user="seanzou",
                password="19970308",
                database="arxiv"
            )
            cursor = conn.cursor()

            # 查询articles表
            cursor.execute("""
                SELECT title, summary, authors, categories, comment, entry_id, journal_ref, updated, CN_title, CN_summary
                FROM arxiv_daily
                ORDER BY updated DESC
                """)
            articles = cursor.fetchall()

            # 开始构建HTML响应
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # HTML页面的开始部分（头部和开头的<body>）
            html = """
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
    _              _                         _    ___ 
   / \   _ ____  _(_)_   ___    ___ ___     / \  |_ _|
  / _ \ | '__\ \/ / \ \ / (_)  / __/ __|   / _ \  | | 
 / ___ \| |   >  <| |\ V / _  | (__\__ \_ / ___ \ | | 
/_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)_/   \_\___|
    </pre>
    <h1>Arxiv: cs.AI</h1>
    """
            html += f"""
                <p>今日文章总数: {len(articles)}</p>
                <p>更新时间: {articles[0][-3]}</p>
                <!--<p>预计阅读英文摘要时间: {15}分钟</p>-->
                <!--<p>预计阅读中文摘要时间: {10}分钟</p>-->
                <!-- 这里可以添加更多信息 -->
                """
            html += """
</div>

<div class="content">
    <div class="inner-content">
            """

            # 遍历所有文章，将它们添加到HTML中
            # 遍历所有文章，将它们添加到HTML中
            for article in articles:
                title, summary, authors, categories, comment, entry_id, journal_ref, updated, CN_title, CN_summary = article
                html += "<div class=\"article-container\">"
                # 英文内容（左侧）
                html += f"<div class=\"article-left\"><h3 class=\"article-title\">Title: {title}</h3><p class=\"article-summary\">Summary: {summary}</p><p><i>Updated: {updated}</i></p></div>"
                # 中文内容（右侧）
                html += f"""
                <div class=\"article-right\"><h3 class=\"article-title\">标题: {CN_title}</h3><p class=\"article-summary\">摘要: {CN_summary}</p>
                <p><i>更新时间: {updated}</i></p>
                <p><i>领域: {categories}</i></p>
                <p><i>下载: <a href="{entry_id}" target="_blank">{entry_id}</a></i></p>
                </div>
                """
                html += "</div>"


            # HTML页面的结尾部分
            html += """
        </div>
    </div>

    <div class="site-info">
        Xinhai (Sean) Zou 粤ICP备20040781号. <br/>
        This website does not contain any JavaScript code. <br/>
    </div>

    </body>
    </html>
            """

            self.wfile.write(html.encode("utf-8"))

        except mysql.connector.Error as e:
            print(e)
        
        finally:
            cursor.close()
            conn.close()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
