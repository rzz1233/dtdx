# 使用Python实现一个简单的HTTP服务器

import http.server
import socketserver

# 设置端口
PORT = 8000

# 创建处理请求的类
Handler = http.server.SimpleHTTPRequestHandler

# 创建一个服务器对象
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    try:
        # 启动服务器，直到手动停止
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.server_close()  # 关闭服务器


# 在终端中运行
# python simple_http_server.py

