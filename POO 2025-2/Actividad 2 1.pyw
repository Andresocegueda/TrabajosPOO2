import tkinter as tk
from tkinter import font
from tkinter import messagebox

# Define una excepción personalizada para errores de la aplicación
class NegativeNumberError(Exception):
    """Excepción para operaciones con números negativos."""
    pass

# --- Clase Principal de la Calculadora ---
class Calculadora:
    """
    Clase que encapsula la interfaz gráfica y la lógica de una calculadora.
    """
    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        master.title("Calculadora")
        master.resizable(False, False)
        master.configure(bg="#2E2E2E")

        # Atributos de estado y configuración de fuentes
        self.expresion = ""
        self.entrada_texto = tk.StringVar()
        self.fuente_display = font.Font(family='Consolas', size=28, weight='bold')
        self.fuente_botones = font.Font(family='Segoe UI', size=16, weight='bold')

        # Creación de los componentes de la interfaz
        self.crear_widgets()

        # Centra la ventana en la pantalla al iniciar
        self.centrar_ventana()

    def crear_widgets(self):
        """
        Crea y posiciona la pantalla y los botones en la ventana.
        """
        # Contenedor para la pantalla
        pantalla_frame = tk.Frame(self.master, bg="#2E2E2E")
        pantalla_frame.pack()

        pantalla = tk.Entry(
            pantalla_frame,
            font=self.fuente_display,
            textvariable=self.entrada_texto,
            fg="#000000",
            bg="#ECECEC",
            bd=0,
            justify='right',
            insertwidth=0,
            state='readonly'
        )
        pantalla.grid(row=0, column=0, ipady=20, pady=(20, 10), padx=10)

        # Contenedor para la matriz de botones
        botones_frame = tk.Frame(self.master, bg="#2E2E2E")
        botones_frame.pack()

        # Definición de la matriz de botones: (texto, fila, col, [colspan], [color])
        botones = [
            ('C', 0, 0, 2, '#D32F2F'), ('/', 0, 2, 1, '#F57C00'), ('*', 0, 3, 1, '#F57C00'),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3, 1, '#F57C00'),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3, 1, '#F57C00'),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3, 1, '#4CAF50'),
            ('0', 4, 0, 2), ('.', 4, 2)
        ]

        # Itera sobre la definición para crear cada botón
        for boton in botones:
            texto, fila, col = boton[0], boton[1], boton[2]
            colspan = boton[3] if len(boton) > 3 else 1
            color = boton[4] if len(boton) > 4 else '#616161'

            accion = lambda x=texto: self.presionar_tecla(x)

            btn = tk.Button(
                botones_frame, text=texto, font=self.fuente_botones, fg="#FFFFFF",
                bg=color, bd=0, padx=20, pady=20, activebackground="#757575",
                activeforeground="#FFFFFF", command=accion
            )
            btn.grid(row=fila, column=col, columnspan=colspan, padx=5, pady=5, sticky='nsew')

    def presionar_tecla(self, tecla):
        """
        Maneja el evento de clic para cualquier botón de la calculadora.
        """
        try:
            if tecla == '=':
                self.calcular_resultado()
            elif tecla == 'C':
                self.expresion = ""
                self.entrada_texto.set("")
            else:
                self.expresion += str(tecla)
                self.entrada_texto.set(self.expresion)
                
        except (NegativeNumberError, ZeroDivisionError, SyntaxError, ValueError) as e:
            # Muestra el error en una ventana emergente y limpia la entrada
            messagebox.showerror("Error de Cálculo", f"{e}" if str(e) else "Error de Sintaxis")
            self.expresion = ""
            self.entrada_texto.set("")
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"{e}")
            self.expresion = ""
            self.entrada_texto.set("")

    def calcular_resultado(self):
        """
        Evalúa la expresión matemática actual y maneja la lógica de errores.
        """
        if not self.expresion:
            return

        # Validación para no permitir números negativos en las operaciones
        if '-' in self.expresion[1:]:
            for i in range(1, len(self.expresion)):
                if self.expresion[i] == '-' and self.expresion[i-1] in ['+', '-', '*', '/']:
                    raise NegativeNumberError("No se permiten números negativos.")
        if self.expresion.startswith('-'):
            raise NegativeNumberError("No se permiten números negativos.")

        resultado = eval(self.expresion)
        self.entrada_texto.set(str(resultado))
        self.expresion = str(resultado)

    def centrar_ventana(self):
        """
        Calcula la posición para centrar la ventana en la pantalla.
        """
        self.master.update_idletasks()
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# --- Bloque de Ejecución Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()