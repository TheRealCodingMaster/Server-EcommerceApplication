import os
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

class SecureHTTPServer:
    def __init__(self, server_address, cert_file, key_file):
        self.server_address = server_address
        self.cert_file = cert_file
        self.key_file = key_file
        self.httpd = None
        logging.basicConfig(level=logging.INFO)

    def start_server(self):
        # Create HTTP server
        self.httpd = HTTPServer(self.server_address, SimpleHTTPRequestHandler)
        
        # Configure SSL context
        self.httpd.socket = ssl.wrap_socket(
            self.httpd.socket,
            server_side=True,
            certfile=self.cert_file,
            keyfile=self.key_file,
            ssl_version=ssl.PROTOCOL_TLS
        )

        logging.info(f"Starting HTTPS server on {self.server_address[0]}:{self.server_address[1]}")
        self.httpd.serve_forever()

    def stop_server(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            logging.info("HTTPS server stopped.")

# Example usage:
if __name__ == '__main__':
    cert_file_path = 'ssl_certificate.pem'  # Update the path accordingly
    key_file_path = 'ssh_key.pem'           # Update the path accordingly
    server_address = ('0.0.0.0', 4443)
    
    secure_server = SecureHTTPServer(server_address, cert_file_path, key_file_path)
    
    try:
        secure_server.start_server()
    except KeyboardInterrupt:
        secure_server.stop_server()
