import tkinter as tk
from tkinter import ttk
from multiprocessing import Process, Manager
import random
import time

# -------- Simulación de ejecución de un proceso --------
def ejecutar_proceso(pid, rafaga, inicio_real, resultados, llegada):
    """Simula la ejecución de un proceso con ráfaga de CPU."""
    tiempo_inicio = time.time() - inicio_real
    time.sleep(rafaga / 1000)  # Convertir ms a segundos
    tiempo_final = time.time() - inicio_real

    turnaround = tiempo_final - llegada
    waiting = turnaround - (rafaga / 1000)
    response = tiempo_inicio - llegada

    resultados.append({
        "PID": pid,
        "Llegada": round(llegada, 3),
        "Inicio": round(tiempo_inicio, 3),
        "Final": round(tiempo_final, 3),
        "Ráfaga(ms)": rafaga,
        "Turnaround": round(turnaround, 3),
        "Waiting": round(waiting, 3),
        "Response": round(response, 3)
    })

# -------- Algoritmos de planificación --------
def planificar_fcfs(procesos):
    return sorted(procesos, key=lambda x: x["llegada"])

def planificar_sjf(procesos):
    return sorted(procesos, key=lambda x: x["rafaga"])

# -------- Función principal de simulación --------
def simular(num_procesos, algoritmo, tree):
    tree.delete(*tree.get_children())  # Limpiar tabla

    # Generar procesos
    procesos = []
    llegada = 0
    for i in range(1, num_procesos + 1):
        rafaga = random.randint(50, 500)  # en ms
        procesos.append({"pid": i, "rafaga": rafaga, "llegada": llegada})
        llegada += random.uniform(0.05, 0.2)  # llegada simulada

    # Ordenar según algoritmo
    if algoritmo == "FCFS":
        cola = planificar_fcfs(procesos)
    else:
        cola = planificar_sjf(procesos)

    # Ejecución
    with Manager() as manager:
        resultados = manager.list()
        inicio_real = time.time()

        procesos_mp = []
        tiempo_actual = 0
        for p in cola:
            # Esperar hasta el tiempo de llegada
            if p["llegada"] > tiempo_actual:
                time.sleep(p["llegada"] - tiempo_actual)
            tiempo_actual = max(tiempo_actual, p["llegada"])

            proc = Process(target=ejecutar_proceso,
                           args=(p["pid"], p["rafaga"], inicio_real, resultados, p["llegada"]))
            proc.start()
            proc.join()  # Para simular CPU compartida

        # Mostrar resultados
        res_ordenados = sorted(resultados, key=lambda x: x["PID"])
        total_ta = total_wt = total_rt = 0
        for r in res_ordenados:
            tree.insert("", "end", values=(
                r["PID"], r["Llegada"], r["Inicio"], r["Final"],
                r["Ráfaga(ms)"], r["Turnaround"], r["Waiting"], r["Response"]
            ))
            total_ta += r["Turnaround"]
            total_wt += r["Waiting"]
            total_rt += r["Response"]

        # Promedios
        n = len(res_ordenados)
        tree.insert("", "end", values=(
            "PROM", "-", "-", "-",
            "-", round(total_ta/n, 3), round(total_wt/n, 3), round(total_rt/n, 3)
        ))

# -------- Interfaz Tkinter --------
def main():
    root = tk.Tk()
    root.title("Simulador de Planificación de CPU")
    root.geometry("800x400")

    # Frame de controles
    frame_ctrl = tk.Frame(root)
    frame_ctrl.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    tk.Label(frame_ctrl, text="Número de procesos:").pack(side=tk.LEFT)
    entry_procs = tk.Entry(frame_ctrl, width=5)
    entry_procs.pack(side=tk.LEFT, padx=5)
    entry_procs.insert(0, "5")

    tk.Label(frame_ctrl, text="Algoritmo:").pack(side=tk.LEFT)
    combo_algo = ttk.Combobox(frame_ctrl, values=["FCFS", "SJF"], state="readonly", width=10)
    combo_algo.current(0)
    combo_algo.pack(side=tk.LEFT, padx=5)

    btn_run = tk.Button(frame_ctrl, text="Simular",
                        command=lambda: simular(int(entry_procs.get()), combo_algo.get(), tree))
    btn_run.pack(side=tk.LEFT, padx=5)

    # Tabla de resultados
    cols = ["PID", "Llegada", "Inicio", "Final", "Ráfaga(ms)", "Turnaround", "Waiting", "Response"]
    tree = ttk.Treeview(root, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=90)
    tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
