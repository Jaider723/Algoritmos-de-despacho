import matplotlib.pyplot as plt
import pandas as pd
from proceso import *

def promedio_tiempo_espera(procesos):
    tiempo_espera = 0
    for proceso in procesos:
        tiempo_espera += proceso.tiempo_finalizacion - proceso.llegada - proceso.rafaga
    return tiempo_espera / len(procesos)


def promedio_tiempo_sistema(procesos):
    tiempo_de_sistema = 0  
    for proceso in procesos:
        tiempo_de_sistema += proceso.tiempo_finalizacion - proceso.llegada  
    return tiempo_de_sistema / len(procesos)
    
    
def graficar(procesos, alg):
    nombre = ''
    if alg == 1:
        nombre = 'Algoritmo de despacho SJF'
    elif alg == 2:
        nombre = 'Algoritmo de despacho Prioridad'
    elif alg == 3:
        nombre = 'Algoritmo de despacho FIFO'
        
    plt.figure(figsize=(10, 6))
    for proceso in procesos:
        plt.plot([proceso.tiempo_inicio, proceso.tiempo_finalizacion], [proceso.nombre, proceso.nombre], 
                 marker='o', label=f'{proceso.nombre}')
        plt.text(proceso.tiempo_finalizacion + 0.1, proceso.nombre, f'{proceso.tiempo_finalizacion}s', va='center')

    procesos.sort(key=lambda p: p.nombre)
    data = [[proceso.nombre, proceso.rafaga, proceso.llegada, proceso.prioridad] for proceso in procesos]

    promedio_t_espera = promedio_tiempo_espera(procesos)
    promedio_t_sistema = promedio_tiempo_sistema(procesos)
    
    df = pd.DataFrame(data, columns=['Proceso', 'Ráfaga', 'Tiempo de llegada', 'Prioridad'])
    plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='bottom', bbox=[0, -1, 1, 0.6])

    plt.subplots_adjust(left=0.2, bottom=0.6)  

    plt.text(0.5, -1.1, f'Tiempo promedio de espera: {promedio_t_espera:.2f}', ha='center', va='center', transform=plt.gca().transAxes)
    plt.text(0.5, -1.2, f'Tiempo promedio de sistema: {promedio_t_sistema:.2f}', ha='center', va='center', transform=plt.gca().transAxes)

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Proceso')
    plt.title(nombre)
    plt.grid(True)
    plt.show()