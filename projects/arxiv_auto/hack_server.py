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
                background-color: #0f0f0f; /* 暗色背景 */
                color: #33ff33; /* 黑客绿 */
                font-family: 'Courier New', monospace; /* 使用等宽字体 */
            }

            /* 主内容区使用flex布局，确保内容在页面垂直居中 */
            .content {
                display: flex;
                justify-content: center; /* 水平居中 */
                text-align: left; /* 文本左对齐 */
                padding: 20px; /* 添加一些内边距 */
                min-height: calc(100vh - 60px); /* 减去底部信息栏高度 */
                line-height: 1.5; /* 增加行高 */
            }

            /* 新增内部容器，用于包裹文本内容 */
            .inner-content {
                max-width: 1200px; /* 设置最大宽度，限制内容宽度 */
                width: 100%; /* 宽度自适应，最大不超过800px */
            }

            /* 页脚样式，固定在底部 */
            .site-info {
                position: relative;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #0c0c0c; /* 深色背景 */
                color: #33ff33; /* 文字颜色 */
                text-align: center;
                padding: 10px 0; /* 填充，增加一些空间 */
                font-size: 14px; /* 调整字体大小 */
            }

            pre {
                background-color: #0f0f0f;
                color: #33ff33;
                word-wrap: break-word; /* 使得pre文本在必要时可以换行 */
                white-space: pre-wrap; /* 保持空白符的表现，同时允许文本换行 */
                text-align: center; /* 居中显示pre内容 */
                margin: 20px 0; /* 增加与其他内容的间距 */
            }

            /* 调整链接样式 */
            a {
                color: #33ff33;
                text-decoration: underline;
                font-size: 16px;
                transition: color 0.3s ease-in-out; /* 平滑颜色过渡 */
            }

            a:hover, a:focus {
                color: #28a745; /* 鼠标悬停和聚焦时的颜色 */
                text-decoration: underline; /* 添加下划线 */
            }

            /* 增加滚动条美化（可选） */
            ::-webkit-scrollbar {
                width: 8px;
            }

            ::-webkit-scrollbar-track {
                background: #333;
            }

            ::-webkit-scrollbar-thumb {
                background: #33ff33;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #28a745;
            }

            /* 表格样式 */
            table {
                border-collapse: collapse; /* 让边框合并为一条线 */
                margin: 20px 0; /* 表格与其他内容的间距 */
                font-size: 16px; /* 表格字体大小 */
                width: 100%; /* 表格宽度 */
                max-width: 600px; /* 限制表格的最大宽度 */
            }
            th, td {
                border: 1px solid #33ff33; /* 设置边框颜色 */
                text-align: left; /* 文本左对齐 */
                padding: 8px; /* 单元格内边距 */
            }
            th {
                background-color: #0c0c0c; /* 表头背景颜色 */
            }
            tr:nth-child(even) {
                background-color: #1a1a1a; /* 为偶数行设置背景色 */
            }

            /* 增加标题样式 */
            .section-title {
                font-weight: bold; /* 加粗 */
                color: #33ff33; /* 使用与正文相同的颜色，也可以选择稍微变化的颜色 */
                margin: 30px 0 15px; /* 增加与前后内容的间距 */
                padding-left: 10px; /* 增加左边距 */
                border-left: 3px solid #33ff33; /* 左边框，增加视觉效果 */
                font-size: 20px; /* 增加字体大小 */
            }

            /* 小标题样式 */
            .subsection-title {
                font-weight: bold;
                color: #33ff33;
                margin: 20px 0 10px;
                padding-left: 20px; /* 增加左边距使之与 section-title 区分 */
                font-size: 18px;
            }

            .article-container {
                display: flex;
                justify-content: space-between; /* 确保左右两边的内容分布 */
                margin-bottom: 20px; /* 每篇文章之间的间距 */
            }

            .article-container > div {
                width: 48%; /* 使得两边的容器各占一半宽度，留出中间的空隙 */
            }

            .article-left, .article-right {
                width: 48%; /* 使得左右两边各占一半宽度 */
            }

            .article-title, .article-summary {
                color: #33ff33; /* 文章标题和摘要的颜色 */
            }
            
            }
        </style>
    </head>
    <body>

    <div class="content">
        <div class="inner-content">
            <pre>
     _              _                         _    ___ 
    / \   _ ____  _(_)_   ___    ___ ___     / \  |_ _|
   / _ \ | '__\ \/ / \ \ / (_)  / __/ __|   / _ \  | | 
  / ___ \| |   >  <| |\ V / _  | (__\__ \_ / ___ \ | | 
 /_/   \_\_|  /_/\_\_| \_/ (_)  \___|___(_)_/   \_\___|
            </pre>
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
