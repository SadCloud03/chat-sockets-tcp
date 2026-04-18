import socket 
import threading
from functions.server_functions import client_management

lock = threading.Lock()

class Server:

    def __init__(self, HOST : str, PORT : int):
        self.HOST = HOST
        self.PORT = PORT
        self.clients = []
        self.server_socket = None

    def Create_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        print(f"[server] : [listening in] : {self.HOST} : {self.PORT}")
    
    def Server_loop(self):
        while True:
            client_socket, direction = self.server_socket.accept()
            client_socket.send("[conection] : success".encode())
            with lock:
                self.clients.append(client_socket)
            
            hilo = threading.Thread(
                target=client_management,
                args=(client_socket, direction, self.clients),
                daemon=True
            )
            hilo.start()

