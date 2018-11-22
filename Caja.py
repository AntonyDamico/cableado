class Caja:
    def __init__(self, x, y, anterior=None):
        '''
        La x & y son la posición de la caja en la habitación
        se toma la esquina superior izquierda como 0,0
        Anterior es la caja anterior a la actual
        '''
        self.x = x
        self.y = y
        self.anterior = anterior

    def __str__(self):
        return f'caja en posición X:{self.x} Y:{self.y}'
