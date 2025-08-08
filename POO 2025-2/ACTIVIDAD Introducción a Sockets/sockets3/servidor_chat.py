import socket
import threading
from colorama import init, Fore, Style

init(autoreset=True)

class ServidorChat:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        self.ip = ip
        self.puerto = puerto
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes = []

    def manejar_cliente(self, conexion, direccion):
        print(Fore.GREEN + f"Conexión establecida con: {direccion}")
        conexion.send("Servidor dice: ¡Bienvenido al chat! Escribe 'bye' para salir.".encode())

        while True:
            try:
                datos = conexion.recv(1024).decode()
                if not datos:
                    break
                if datos.lower() == "bye":
                    print(Fore.YELLOW + f"Cliente {direccion} cerró la conexión.")
                    conexion.send("bye".encode())
                    break
                print(Fore.CYAN + f"Cliente {direccion} dice: {datos}")
                mensaje = input(Fore.MAGENTA + "Servidor: ")
                mensaje_con_prefijo = f"Servidor dice: {mensaje}"
                conexion.send(mensaje_con_prefijo.encode())
                if mensaje.lower() == "bye":
                    print(Fore.YELLOW + "Servidor cerró la conexión.")
                    break
            except ConnectionResetError:
                print(Fore.RED + f"Conexión con cliente {direccion} perdida.")
                break

        conexion.close()

    def iniciar_chat(self):
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
        print(Fore.GREEN + f"Servidor escuchando en {self.ip}:{self.puerto}")

        while True:
            conexion, direccion = self.servidor.accept()
            hilo = threading.Thread(target=self.manejar_cliente, args=(conexion, direccion))
            hilo.start()
            self.clientes.append(hilo)

if __name__ == "__main__":
    servidor = ServidorChat()
    servidor.iniciar_chat()
