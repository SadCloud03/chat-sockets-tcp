from server_class import Server


servidor = Server("127.0.0.1", 5000)
servidor.Create_server()
servidor.Server_loop()