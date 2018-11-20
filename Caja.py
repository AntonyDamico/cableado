class Caja:
    def __init__(self, x, y, anterior=None):
        self.x = x
        self.y = y
        self.anterior = anterior

    def __str__(self):
        string = f'\tcaja en {self.x} {self.y}'
        if self.anterior is not None:
            string += f' y anterior {self.anterior}'
        return string
