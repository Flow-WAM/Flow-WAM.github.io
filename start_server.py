"""Lightweight local preview server for the FlowWAM project page.

Run with:
    python3 start_server.py

Then open http://localhost:8012 in your browser. The script also tries to
launch the page in your default browser automatically.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

PORT = 8012

handler = SimpleHTTPRequestHandler
server = HTTPServer(("", PORT), handler)

print(f"FlowWAM site running at http://localhost:{PORT}")
print("Press Ctrl+C to stop the server")

webbrowser.open(f"http://localhost:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
    print("\nServer stopped")
