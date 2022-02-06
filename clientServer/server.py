import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

def server():
    serverPort = ("127.0.0.1", 8080)
    server = ThreadedHandler(serverPort, Handler)
    print(f'Abertura do servidor no endereço {serverPort[0]} e na porta {str(serverPort[1])}')
    server.serve_forever()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        currentThread = threading.currentThread().getName()
        print(f'Serviço prestado pela {currentThread}')  
        self.wfile.write(bytes(currentThread, "utf8")) 
        return

class ThreadedHandler(ThreadingMixIn, HTTPServer):
    pass

server()