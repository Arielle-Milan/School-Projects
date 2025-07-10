#HTTP_Server.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello from HTTP Server!</h1>")

server = HTTPServer(('localhost', 8000), SimpleHandler)
print("Server running on http://localhost:8000")
server.serve_forever()