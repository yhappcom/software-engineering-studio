from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
ROOT=Path(__file__).parent
os.chdir(ROOT)
class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-store, max-age=0')
        super().end_headers()
    def do_GET(self):
        if self.path.split('?',1)[0]=='/sw.js':
            v=(ROOT/'version.txt').read_text().strip()
            body=f"const VERSION='{v}';\nself.addEventListener('install',e=>e.waitUntil(self.skipWaiting()));\nself.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));\nself.addEventListener('message',e=>{{if(e.data==='version'&&e.ports[0])e.ports[0].postMessage(VERSION);}});\n".encode()
            self.send_response(200); self.send_header('Content-Type','application/javascript'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body); return
        super().do_GET()
ThreadingHTTPServer(('127.0.0.1',8769),H).serve_forever()
