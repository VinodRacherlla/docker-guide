# Simple HTTP server without external packages
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/":
            if parsed_url.query:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Error: Query parameters are not allowed.")
            else:
                message = "Welcome to Python running in a container!"
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ("0.0.0.0", 8080)
    httpd = server_class(server_address, handler_class)
    print("Starting simple server on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()