from tkinter import *
from tkinter import colorchooser

class Aplicacion:
    def __init__(self, master):
        self.master = master
        master.title("Dibujo de Figuras")
        master.geometry("450x320")

        self.figura_seleccionada = None
        self.x_click = 0
        self.y_click = 0

        # Color inicial
        self.color_actual = "#ADD8E6"  # lightblue

        # Lista para seleccionar figura
        self.lista_figuras = Listbox(master)
        self.lista_figuras.insert(1, "Círculo")
        self.lista_figuras.insert(2, "Rectángulo")
        self.lista_figuras.insert(3, "Elipse")
        self.lista_figuras.pack(side=LEFT, fill=Y)
        self.lista_figuras.bind("<<ListboxSelect>>", self.seleccionar_figura)

        # Canvas para dibujo
        self.canvas = Canvas(master, bg="white", width=350, height=300)
        self.canvas.pack(side=RIGHT, expand=True, fill=BOTH)
        self.canvas.bind("<Button-1>", self.clic_canvas)

        # Botón para abrir selector de color
        self.btn_color = Button(master, text="Seleccionar color", command=self.seleccionar_color)
        self.btn_color.place(x=10, y=270)

        # Cuadro que muestra el color seleccionado
        self.muestra_color = Canvas(master, bg=self.color_actual, width=50, height=25)
        self.muestra_color.place(x=150, y=270)

        # Botón para borrar
        self.btn_borrar = Button(master, text="Borrar todo", command=self.borrar_todo)
        self.btn_borrar.place(x=10, y=300)

    def seleccionar_figura(self, event):
        seleccion = self.lista_figuras.curselection()
        if seleccion:
            self.figura_seleccionada = self.lista_figuras.get(seleccion[0])

    def clic_canvas(self, event):
        self.x_click, self.y_click = event.x, event.y
        self.dibujar()

    def dibujar(self):
        color = self.color_actual
        if self.figura_seleccionada == "Círculo":
            self.canvas.create_oval(self.x_click-25, self.y_click-25, self.x_click+25, self.y_click+25, fill=color)
        elif self.figura_seleccionada == "Rectángulo":
            self.canvas.create_rectangle(self.x_click-30, self.y_click-20, self.x_click+30, self.y_click+20, fill=color)
        elif self.figura_seleccionada == "Elipse":
            self.canvas.create_oval(self.x_click-30, self.y_click-15, self.x_click+30, self.y_click+15, fill=color)

    def borrar_todo(self):
        self.canvas.delete("all")

    def seleccionar_color(self):
        color_seleccionado = colorchooser.askcolor(initialcolor=self.color_actual)
        if color_seleccionado[1]:  # Si no se cancela
            self.color_actual = color_seleccionado[1]
            self.muestra_color.configure(bg=self.color_actual)

if __name__ == "__main__":
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()