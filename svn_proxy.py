# geocities_proxy.py

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

# --- Configuration ---
PROXY_HOST = "localhost"
PROXY_PORT = 8080 # A different port to simulate the 'www.domain.com'
CONFIG_FILE = "domains.json"

class GeocitiesRedirectHandler(BaseHTTPRequestHandler):
    """
    Handles requests for www.domain.com/{site} and redirects to the 
    corresponding skatlaz_net() instance using data from domains.json.
    """
    
    def do_GET(self):
        # The requested path is usually in the format: /{site}
        path = self.path.strip('/')
        
        if not path:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome to the Geocities Proxy. Access /your_site_name")
            return

        # 1. Read configuration
        try:
            with open(CONFIG_FILE, 'r') as f:
                domains_config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            domains_config = []

        # 2. Find the target URL based on the path (site name)
        target_url = None
        for config in domains_config:
            # We assume 'named_domain' in config matches the site path
            if config.get("named_domain") == path:
                target_url = config.get("local_svn_url")
                break
        
        # 3. Redirect or Error
        if target_url:
            # Send a 302 Found response for temporary redirect
            self.send_response(302) 
            # The Location header tells the client where to go
            self.send_header('Location', target_url) 
            self.end_headers()
            print(f"Redirecting {self.path} to {target_url}")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(f"Site '{path}' not found in configuration.".encode())
            
def skatlaz_geocities():
    """
    Starts the proxy server.
    """
    print(f"--- Starting skatlaz_geocities proxy on http://{PROXY_HOST}:{PROXY_PORT} ---")

    # Use ThreadingTCPServer for better handling
    class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
        pass

    try:
        httpd = ThreadingHTTPServer((PROXY_HOST, PROXY_PORT), GeocitiesRedirectHandler)
        print(f"Proxy serving at http://{PROXY_HOST}:{PROXY_PORT}")
        print("Test URL example: http://localhost:8080/local_svn_repo")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the proxy server...")
        httpd.server_close()

if __name__ == '__main__':
    # skatlaz_geocities() # This will block and run the server
    pass
