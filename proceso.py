class Proceso:
    def __init__(self, nombre, llegada, rafaga, prioridad):
        self.nombre = nombre
        self.llegada = llegada
        self.rafaga = rafaga
        self.prioridad = prioridad
        self.tiempo_inicio = 0
        self.tiempo_finalizacion = 0