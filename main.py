import os
from algoritmos import *
from graficar import *

def agregar_procesos():
    procesos_ag = []
    while True:
        try:
            n = int(input('Ingrese el número de procesos: '))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido para el número de procesos.")

    for i in range(n):
        print(f'P{i+1}:')
        nombre = 'P' + str(i+1)
        while True:
            try:
                llegada = int(input('Tiempo de llegada: '))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido para el tiempo de llegada.")
        while True:
            try:
                rafaga = int(input('Tiempo de ráfaga: '))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido para el tiempo de ráfaga.")
        while True:
            try:
                prioridad = int(input('Prioridad: '))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido para la prioridad.")

        p = Proceso(nombre, llegada, rafaga, prioridad)
        print(f'Proceso {nombre} agregado.')
        procesos_ag.append(p)

    return procesos_ag


def main():
    while True:
        os.system('cls')
        print('''Algoritmos de despacho:
        1. Ingresar procesos
        2. Usar procesos de ejemplo
        0. Salir''')
        opcion = input("Ingrese una opción: ")
        if opcion == '0':
            break
        elif opcion == '1':
            procesos = agregar_procesos()
        elif opcion == '2':
            procesos = [Proceso('P1', 0, 10, 1), Proceso('P2', 2, 6, 2), Proceso('P3', 2, 4, 6 ), Proceso('P4', 3, 8, 4), Proceso('P5', 5, 2, 5)]
        else:
            continue
        procesos.sort(key=lambda x: x.llegada)
        while True:
            procesos_copy = procesos.copy()
            os.system('cls')
            print('''Algoritmos de despacho:
            1. SJF
            2. Prioridad
            3. FIFO
            0. Atras''')
            opcion = input("Ingrese una opción: ")
            if opcion == '1':
                procesos_ejecutados = alg_sjf(procesos_copy)
                graficar(procesos_ejecutados, 1)
            elif opcion == '2':
                procesos_ejecutados = alg_prioridad(procesos_copy)
                graficar(procesos_ejecutados, 2)
            elif opcion == '3':
                procesos_ejecutados = alg_fifo(procesos_copy)
                graficar(procesos_ejecutados, 3)
            elif opcion == '0':
                break
            else:
                continue
            
main()