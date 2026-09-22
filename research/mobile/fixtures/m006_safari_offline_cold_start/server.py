from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent)
class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-store, max-age=0')
        super().end_headers()
ThreadingHTTPServer(('127.0.0.1',8770),H).serve_forever()
