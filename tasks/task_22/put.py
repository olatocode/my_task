from http.server import BaseHTTPRequestHandler,HTTPServer
import json
data = [
    {"id":1,"name":"John Doe","email":"BtWlH@example.com"},
    {"id":2,"name":"Jane Doe","email":"KZ2r0@example.com"}
]

# create put method
class BasicAPI(BaseHTTPRequestHandler):
    def do_PUT(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)
        post_data = json.loads(parsed_data)
        data.append(post_data)  # Saving to database
        self.send_data({
            "Message": "Data Received",
            "data": post_data
        })
    def send_data(self, payload, status = 201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
def run():
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()
print("Application is running")
run()