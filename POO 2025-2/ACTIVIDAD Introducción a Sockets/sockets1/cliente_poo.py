import socket

class Cliente:
    def __init__(self, ip='127.0.0.1', puerto=9001):
        # Dirección IP y puerto del servidor al cual se conectará el cliente
        self.ip = ip
        self.puerto = puerto
        # Crear un socket TCP/IP para el cliente
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def enviar_mensaje(self):
        # Conectarse al servidor con la IP y puerto especificados
        self.cliente.connect((self.ip, self.puerto))
        # Solicitar al usuario que ingrese un mensaje para enviar
        mensaje = input("Escribe un mensaje para el servidor: ")
        # Enviar el mensaje al servidor codificado en bytes
        self.cliente.send(mensaje.encode())
        # Cerrar la conexión después de enviar el mensaje
        self.cliente.close()

if __name__ == "__main__":
    # Crear instancia del cliente y ejecutar el envío de mensaje
    cliente = Cliente()
    cliente.enviar_mensaje()
