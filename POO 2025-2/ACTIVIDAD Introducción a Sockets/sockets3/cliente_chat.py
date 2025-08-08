import socket
from colorama import init, Fore, Style

init(autoreset=True)

class ClienteChat:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        self.ip = ip
        self.puerto = puerto
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar_chat(self):
        self.cliente.connect((self.ip, self.puerto))
        print(Fore.GREEN + "Conectado al servidor. Escribe 'bye' para salir.")

        while True:
            mensaje = input(Fore.MAGENTA + "Cliente: ")
            mensaje_con_prefijo = f"Cliente dice: {mensaje}"
            self.cliente.send(mensaje_con_prefijo.encode())

            if mensaje.lower() == "bye":
                print(Fore.YELLOW + "Cliente cerró la conexión.")
                break

            respuesta = self.cliente.recv(1024).decode()
            if respuesta.lower() == "bye":
                print(Fore.YELLOW + "El servidor ha cerrado la conexión.")
                break
            print(Fore.CYAN + respuesta)

        self.cliente.close()

if __name__ == "__main__":
    cliente = ClienteChat()
    cliente.iniciar_chat()
