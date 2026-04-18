import threading
from funciones.funciones_cliente import escuchar_mensajes, conectar

class client:

    def __init__(self, IP_SERVER, PORT_SERVER):
        self.IP_SERVER = IP_SERVER
        self.PORT_SERVER = PORT_SERVER
        self.socket_cliente = None
        self.nombre_cliente = None

    
    def Crear_cliente(self):
        self.socket_cliente = conectar(self.PORT_SERVER, self.IP_SERVER)

        self.nombre_cliente = input("Escriba su nombre: ")

        if self.nombre_cliente == "":
            self.nombre_cliente = "Desconocido"

        try: 
            self.socket_cliente.send(f"[conectando] : {self.nombre_cliente}".encode())
            print("[for exit] : './salir'\n[for reconecting] : './reconnect'\n[see help] : './help'")
        except (Exception, KeyboardInterrupt) as e:
            print(f"[error] : {e}")


    def Bucle_cliente_servidor(self):

        hilo = threading.Thread(
            target=escuchar_mensajes,
            args=(self.socket_cliente,),
            daemon=True
        )

        hilo.start()

        while True:
            try:
                mensaje = input()

                if mensaje == "./salir":
                    self.socket_cliente.send(f"[{self.nombre_cliente}] : [desconection]".encode())
                    self.socket_cliente.close()
                    break

                elif mensaje == "./reconnect":
                    print("[reconecting]")
                    self.socket_cliente = conectar(self.PORT_SERVER, self.IP_SERVER)

                elif mensaje == "./help":
                    print("[for exit] : './salir'\n[for reconecting] : './reconnect'\n[see help] : './help'")
                    continue
                    
                self.socket_cliente.send(f"[{self.nombre_cliente}] : [message] : {mensaje}".encode())
            
            except (Exception, KeyboardInterrupt) as e:
                print(f"[error] : {e}")
                desicion = input("[message] : desea salir (s/n): ").lower()
                if desicion == "s":
                    print("[closed conection]")
                    break
            
        if self.socket_cliente:
            self.socket_cliente.close()
        
        print("[closed client]")
