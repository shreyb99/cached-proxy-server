import http.server
import socketserver
import urllib.request
import shutil
import os
import hashlib
import sys


class CacheHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        m = hashlib.md5()
        m.update(self.path.encode("utf-8"))
        cache_filename = m.hexdigest() + ".cached"

        if not os.path.exists(cache_filename):
            print("cache miss")
            with open(cache_filename + ".temp", "wb") as output:
                req = urllib.request.Request("http:/" + self.path)
                # copy request headers
                for k in self.headers:
                    if k not in ["Host"]:
                        req.add_header(k, self.headers[k])
                try:
                    resp = urllib.request.urlopen(req)
                    shutil.copyfileobj(resp, output)
                    os.rename(cache_filename + ".temp", cache_filename)
                except urllib.error.HTTPError as err:
                    self.send_response(err.code)
                    self.end_headers()
                    return
        else:
            print("cache hit")

        with open(cache_filename, "rb") as cached:
            self.send_response(200)
            self.end_headers()
            shutil.copyfileobj(cached, self.wfile)


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8000), CacheHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
