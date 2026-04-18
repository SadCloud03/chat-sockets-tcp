from client_class import client


cliente = client(5000, "127.0.0.1")
cliente.Crear_cliente()
cliente.Bucle_cliente_servidor()