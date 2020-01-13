# -*- coding: UTF-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import unquote
import sql
 
class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/text')
        self.end_headers()
        print("path:",self.path)
        if self.path!='/favicon.ico':
            rt=sql.AddLog(unquote(self.path[1:],encoding='utf-8'))
            self.wfile.write(rt.encode('utf-8'))

if __name__ == '__main__':
    host = ('', 80)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()