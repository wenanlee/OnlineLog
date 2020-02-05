# -*- coding: UTF-8 -*-
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import sql


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', ' text/html')
        self.end_headers()
        paths = unquote(self.path, encoding='utf-8').split('?')
        html = ''
        print("path:", paths)
        if paths[0] == '/favicon.ico':
            pass
        elif paths[0] == '/select':
            html = sql.GetLog(paths[1])
        elif paths[0] == '/insert':
            html = sql.AddLog(paths[1])
            # html=sql.AddLog('{"name":"测试软件","log":[{"level":1,"info":"测试消息1"},{"level":2,"info":"测试消息2"}]}')
        else:
            html = '未知命令'
        self.wfile.write(html.encode('utf-8'))


if __name__ == '__main__':
    host = ('', 80)
    #自定义端口
    if '-p' in sys.argv:
        host = ('', int(sys.argv[sys.argv.index('-p')+1]))
    #后台运行
    if '-d' in sys.argv:
        pass
    #把日志导出到文件
    if '-f' in sys.argv:
        pass
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()