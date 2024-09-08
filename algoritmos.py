from proceso import *

def alg_fifo(procesos):
    procesos_ejecutados = []
    tiempo_actual = 0
    while procesos:
        proceso = procesos.pop(0)
        if proceso.llegada > tiempo_actual:
            tiempo_actual = proceso.llegada

        proceso.tiempo_inicio = tiempo_actual
        proceso.tiempo_finalizacion = tiempo_actual + proceso.rafaga
        tiempo_actual += proceso.rafaga
        procesos_ejecutados.append(proceso)
        
    return procesos_ejecutados


def alg_sjf(procesos):
    procesos_ejecutados = []
    tiempo_actual = 0
    pila = []
    while procesos or pila:
        for proceso in procesos[:]:
            if proceso.llegada <= tiempo_actual:
                pila.append(proceso)
                procesos.remove(proceso)

        if pila:
            pila.sort(key=lambda x: x.rafaga)
            proceso = pila.pop(0)
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_finalizacion = tiempo_actual + proceso.rafaga
            tiempo_actual += proceso.rafaga
            procesos_ejecutados.append(proceso)
        else:
            tiempo_actual += 1
    return procesos_ejecutados


#En este algortimo se toma como proceso con mayor prioridad al que tenga un valor menor en su atributo prioridad
def alg_prioridad(procesos):
    procesos_ejecutados = []
    tiempo_actual = 0
    pila = []
    while procesos or pila:
        for proceso in procesos[:]:
            if proceso.llegada <= tiempo_actual:
                pila.append(proceso)
                procesos.remove(proceso)

        if pila:
            pila.sort(key=lambda x: x.prioridad)
            proceso = pila.pop(0)
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_finalizacion = tiempo_actual + proceso.rafaga
            tiempo_actual += proceso.rafaga
            procesos_ejecutados.append(proceso)
        else:
            tiempo_actual += 1
    return procesos_ejecutados