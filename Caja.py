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
        '''
        Calcula la distancia de la caja actual a la caja principal
        sumando el x & y para llegar a la habitación y
        el x & y para llegar a la caja dentro de la habitación
        '''
        distancia_a_hab = self.habitacion.x + self.habitacion.y
        distancia_a_caja = distancia_a_hab + self.x + self.y
        return distancia_a_caja

    def __str__(self):
        return f'caja en posición X:{self.x} Y:{self.y}'


    '''
    función recursiva para encontrar la habitación principal
    en el caso de que la necesite
    '''
    # def get_hab_principal(self, hab):
    #     hab_anterior = hab.hab_anterior
    #     if hab_anterior is not None:
    #         hab = self.get_hab_principal(hab_anterior)
    #     return hab