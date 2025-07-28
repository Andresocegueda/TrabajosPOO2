import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class LineaProduccion(threading.Thread):
    def __init__(self, nombre, callbacks, piezas=10):
        super().__init__()
        self.nombre = nombre
        self.actualizar_estado = callbacks['estado']
        self.actualizar_contador = callbacks['contador']
        self.actualizar_progreso = callbacks['progreso']
        self.piezas = piezas
        self._detener = False

    def detener(self):
        self._detener = True

    def run(self):
        try:
            self.actualizar_contador(1)
            for i in range(1, self.piezas + 1):
                if self._detener:
                    self.actualizar_estado(self.nombre, "⛔ Producción detenida por el usuario.")
                    return
                time.sleep(random.uniform(0.5, 1.2))

                # Falla técnica con 30% de probabilidad
                if random.random() < 0.3:
                    raise Exception("❌ Falla técnica inesperada.")

                self.actualizar_estado(self.nombre, f"Produciendo pieza {i}/{self.piezas}")
                progreso = int((i / self.piezas) * 100)
                self.actualizar_progreso(self.nombre, progreso)

            self.actualizar_estado(self.nombre, "✔️ Producción completada exitosamente")
            self.actualizar_progreso(self.nombre, 100)
        except Exception as e:
            self.actualizar_estado(self.nombre, f"{str(e)}")
        finally:
            self.actualizar_contador(-1)

class SimuladorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Fábrica Concurrente")
        self.lineas = {}
        self.hilos_activos = 0

        self.frame_superior = tk.Frame(master)
        self.frame_superior.pack(pady=10)

        self.entrada_nombre = tk.Entry(self.frame_superior, width=30)
        self.entrada_nombre.pack(side=tk.LEFT, padx=5)
        self.entrada_nombre.insert(0, "Línea A")

        self.boton_agregar = tk.Button(self.frame_superior, text="Agregar línea", command=self.agregar_linea)
        self.boton_agregar.pack(side=tk.LEFT, padx=5)

        self.boton_iniciar = tk.Button(master, text="Iniciar producción", command=self.iniciar_produccion)
        self.boton_iniciar.pack(pady=5)

        self.boton_detener = tk.Button(master, text="Detener todas las líneas", command=self.detener_todas)
        self.boton_detener.pack(pady=5)

        self.etiqueta_hilos = tk.Label(master, text="Hilos activos: 0")
        self.etiqueta_hilos.pack()

        self.area_resultados = tk.Frame(master)
        self.area_resultados.pack()

    def agregar_linea(self):
        nombre = self.entrada_nombre.get().strip()
        if not nombre or nombre in self.lineas:
            return

        frame = tk.Frame(self.area_resultados)
        frame.pack(pady=3, fill="x")

        estado = tk.Label(frame, text=f"{nombre}: En espera", anchor="w", width=50)
        estado.pack()

        barra = ttk.Progressbar(frame, length=300)
        barra.pack(pady=2)

        self.lineas[nombre] = {
            "estado": estado,
            "progreso": barra,
            "thread": None
        }

        self.entrada_nombre.delete(0, tk.END)

    def actualizar_estado(self, nombre, mensaje):
        if nombre in self.lineas:
            self.lineas[nombre]["estado"].config(text=f"{nombre}: {mensaje}")

    def actualizar_progreso(self, nombre, valor):
        if nombre in self.lineas:
            self.lineas[nombre]["progreso"]["value"] = valor

    def actualizar_contador_hilos(self, cambio):
        self.hilos_activos += cambio
        self.etiqueta_hilos.config(text=f"Hilos activos: {self.hilos_activos}")

    def iniciar_produccion(self):
        for nombre, datos in self.lineas.items():
            hilo = datos["thread"]
            if hilo is None or not hilo.is_alive():
                nueva_linea = LineaProduccion(
                    nombre,
                    {
                        "estado": self.actualizar_estado,
                        "contador": self.actualizar_contador_hilos,
                        "progreso": self.actualizar_progreso
                    }
                )
                datos["thread"] = nueva_linea
                nueva_linea.start()

    def detener_todas(self):
        for datos in self.lineas.values():
            hilo = datos["thread"]
            if hilo and hilo.is_alive():
                hilo.detener()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorApp(root)
    root.mainloop()
