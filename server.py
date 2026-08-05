import http.server
import socketserver
import os
import urllib.parse

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
STUDY_DIR = r"D:\Study\R.O.R. Cards Day and Night Signals"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Intercept and map night signals images
        if path.startswith("/images/night/"):
            filename = os.path.basename(path)
            local_path = os.path.join(STUDY_DIR, "NightSignals", filename)
            self.serve_file(local_path, "image/gif")
            return
            
        # Intercept and map day signals images
        if path.startswith("/images/day/"):
            filename = os.path.basename(path)
            local_path = os.path.join(STUDY_DIR, "DaySignals", filename)
            self.serve_file(local_path, "image/gif")
            return
            
        # Delegate standard requests to SimpleHTTPRequestHandler
        super().do_GET()

    def serve_file(self, file_path, content_type):
        if not os.path.exists(file_path):
            self.send_error(404, f"File not found: {file_path}")
            return
        
        try:
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(os.path.getsize(file_path)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")

if __name__ == "__main__":
    # Create the server
    handler = CustomHandler
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving R.O.R. App at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
