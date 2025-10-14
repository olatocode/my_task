from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name": "Sam Larry",
        "track": "A1 Eng"
    }
]
  
class BasicAPI(BaseHTTPRequestHandler):
  def send_data(self, data, status = 200):
    self.send_response(status)
    self.send_header("Content-Tpye", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode())

  def do_GET(self):
      self.send_data(data)
      

def run():
        HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is runing")
run()