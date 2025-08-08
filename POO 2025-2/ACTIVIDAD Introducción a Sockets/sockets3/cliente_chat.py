import socket
from colorama import init, Fore, Style

# Inicializa colorama para que funcione en todas las plataformas
init(autoreset=True)

class ClienteChat:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        # Dirección IP y puerto a los que se conectará el cliente
        self.ip = ip
        self.puerto = puerto
        # Crear un socket TCP/IP para el cliente
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar_chat(self):
        # Conectarse al servidor usando la IP y puerto configurados
        self.cliente.connect((self.ip, self.puerto))
        print(Fore.GREEN + "Conectado al servidor. Escribe 'bye' para salir.")

        while True:
            # Leer mensaje del usuario para enviar al servidor
            mensaje = input(Fore.MAGENTA + "Cliente: ")
            # Añadir prefijo automático al mensaje
            mensaje_con_prefijo = f"Cliente dice: {mensaje}"
            # Enviar mensaje al servidor codificado en bytes
            self.cliente.send(mensaje_con_prefijo.encode())

            if mensaje.lower() == "bye":
                # Si el cliente escribe 'bye', cerrar conexión y terminar chat
                print(Fore.YELLOW + "Cliente cerró la conexión.")
                break

            # Esperar respuesta del servidor
            respuesta = self.cliente.recv(1024).decode()
            if respuesta.lower() == "bye":
                # Si el servidor indica cierre, terminar chat
                print(Fore.YELLOW + "El servidor ha cerrado la conexión.")
                break
            # Mostrar la respuesta del servidor con color cyan
            print(Fore.CYAN + respuesta)

        # Cerrar socket del cliente
        self.cliente.close()

if __name__ == "__main__":
    # Crear instancia del cliente y arrancar el chat
    cliente = ClienteChat()
    cliente.iniciar_chat()
