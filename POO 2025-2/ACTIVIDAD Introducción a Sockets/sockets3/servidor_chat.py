import socket
import threading
from colorama import init, Fore, Style

# Inicializa colorama para que funcione en todas las plataformas
init(autoreset=True)

class ServidorChat:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        # Dirección IP y puerto en los que escuchará el servidor
        self.ip = ip
        self.puerto = puerto
        # Crear un socket TCP/IP
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Lista para guardar los hilos que manejarán clientes múltiples
        self.clientes = []

    def manejar_cliente(self, conexion, direccion):
        # Método que se ejecuta en un hilo para atender a cada cliente conectado
        print(Fore.GREEN + f"Conexión establecida con: {direccion}")

        # Enviar mensaje de bienvenida al cliente
        conexion.send("Servidor dice: ¡Bienvenido al chat! Escribe 'bye' para salir.".encode())

        while True:
            try:
                # Esperar mensaje del cliente
                datos = conexion.recv(1024).decode()
                if not datos:
                    # Si no se recibe nada, romper el ciclo (cliente desconectado)
                    break
                if datos.lower() == "bye":
                    # Si el cliente escribe 'bye', cerrar conexión
                    print(Fore.YELLOW + f"Cliente {direccion} cerró la conexión.")
                    conexion.send("bye".encode())  # Confirmar cierre al cliente
                    break
                # Mostrar mensaje recibido en consola del servidor con color cyan
                print(Fore.CYAN + f"Cliente {direccion} dice: {datos}")

                # Leer mensaje que el servidor desea enviar
                mensaje = input(Fore.MAGENTA + "Servidor: ")
                # Añadir prefijo automático al mensaje
                mensaje_con_prefijo = f"Servidor dice: {mensaje}"
                # Enviar mensaje al cliente
                conexion.send(mensaje_con_prefijo.encode())

                if mensaje.lower() == "bye":
                    # Si el servidor escribe 'bye', cerrar conexión
                    print(Fore.YELLOW + "Servidor cerró la conexión.")
                    break
            except ConnectionResetError:
                # Manejo en caso de que el cliente desconecte abruptamente
                print(Fore.RED + f"Conexión con cliente {direccion} perdida.")
                break

        # Cerrar conexión con el cliente
        conexion.close()

    def iniciar_chat(self):
        # Configurar el socket para que escuche conexiones entrantes
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
        print(Fore.GREEN + f"Servidor escuchando en {self.ip}:{self.puerto}")

        while True:
            # Aceptar conexión de un cliente nuevo
            conexion, direccion = self.servidor.accept()
            # Crear un hilo para manejar a este cliente de forma independiente
            hilo = threading.Thread(target=self.manejar_cliente, args=(conexion, direccion))
            hilo.start()
            # Guardar referencia del hilo en lista (opcional, para control)
            self.clientes.append(hilo)

if __name__ == "__main__":
    # Crear instancia del servidor y arrancar el chat
    servidor = ServidorChat()
    servidor.iniciar_chat()

