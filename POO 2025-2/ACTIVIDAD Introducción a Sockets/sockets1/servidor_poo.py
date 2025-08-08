import socket

class Servidor:
    def __init__(self, ip='127.0.0.1', puerto=9001):
        # Dirección IP y puerto donde el servidor escuchará conexiones
        self.ip = ip
        self.puerto = puerto
        # Crear un socket TCP/IP para el servidor
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        # Vincular el socket a la dirección IP y puerto especificados
        self.servidor.bind((self.ip, self.puerto))
        # Poner el socket en modo escucha, con hasta 5 conexiones en cola
        self.servidor.listen(5)
        print(f"Servidor escuchando en {self.ip}:{self.puerto}")
        # Aceptar una conexión entrante
        conexion, direccion = self.servidor.accept()
        print("Conexión establecida con:", direccion)
        # Recibir datos enviados por el cliente (hasta 1024 bytes)
        datos = conexion.recv(1024)
        print("Mensaje recibido:", datos.decode())
        # Cerrar la conexión con el cliente
        conexion.close()

if __name__ == "__main__":
    # Crear instancia del servidor y arrancar la escucha
    servidor = Servidor()
    servidor.iniciar()

