import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello from server!")
        return
    
class CustomHTTPServer(HTTPServer):
    def __init__(self,host,port):
        server_address=(host,port)
        HTTPServer.__init__(self, server_address, RequestHandler)
        
