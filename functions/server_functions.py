import threading

lock = threading.Lock()


def do_broadcast(client_socket, message, clients):
    with lock:
        for client in clients:
            if client != client_socket:
                try:
                    client.send(message)
                except:
                    clients.remove(client)



def client_management(client_socket, direction, clients):
    print(f"[new client] : [{direction}]")
    while True:
        try:
            mensaje = client_socket.recv(1024)
            print(mensaje.decode())
            
            if not mensaje:
                break

            do_broadcast(client_socket, mensaje, clients)
        except:
            break
    
    with lock:
        clients.remove(client_socket)

    print(f"[desconection] : {direction}")
    client_socket.close()