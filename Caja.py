class Caja:
    def __init__(self, x, y, habitacion, caja_anterior=None):
        '''
        La x & y son la posición de la caja en la habitación
        se toma la esquina superior izquierda como 0,0
        Anterior es la caja anterior a la actual
        '''
        self.x = x
        self.y = y
        self.caja_anterior = caja_anterior
        self.habitacion = habitacion
        self.distancia_a_principal = self.calcular_distancia_principal()

    def calcular_distancia_principal(self):
        distancia_a_hab = self.habitacion.x + self.habitacion.y
        distancia_a_caja = distancia_a_hab + self.x + self.y
        return distancia_a_caja

    def __str__(self):
        return f'caja en posición X:{self.x} Y:{self.y}'
