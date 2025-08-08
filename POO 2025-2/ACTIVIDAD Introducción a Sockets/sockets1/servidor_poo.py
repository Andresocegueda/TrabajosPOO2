import socket

class Servidor:
    def __init__(self, ip='127.0.0.1', puerto=9001):
        self.ip = ip
        self.puerto = puerto
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
        print(f"Servidor escuchando en {self.ip}:{self.puerto}")
        conexion, direccion = self.servidor.accept()
        print("Conexión establecida con:", direccion)
        datos = conexion.recv(1024)
        print("Mensaje recibido:", datos.decode())
        conexion.close()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
