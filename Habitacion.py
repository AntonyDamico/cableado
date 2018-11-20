from Caja import Caja


class Habitacion:
    def __init__(self, computadoras, x, y, ancho, alto, hab_anterior=None):
        self.computadoras = computadoras
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.cajas = []
        self.principal = False
        if hab_anterior is not None:
            self.hab_anterior = hab_anterior
            self.agregar_caja()
            if not hab_anterior.principal and self.cambio_orientacion():
                print('no es la misma')
                # self.hab_anterior.agregar_caja()

    def agregar_caja_principal(self, x, y):
        self.principal = True
        caja_principal = Caja(x, y)
        self.cajas.append(caja_principal)

    def agregar_caja(self):
        nueva_caja = self.crear_caja()
        self.cajas.append(nueva_caja)

    def crear_caja(self):
        if not self.cajas:
            caja_anterior = self.hab_anterior.cajas[-1]
            return Caja(caja_anterior.x, caja_anterior.y, caja_anterior)

    def check_orientacion(self):
        if self.hab_anterior is not None:
            if self.hab_anterior.x != self.x:
                return 'horizontal'
            if self.hab_anterior.y != self.y:
                return 'vertical'
        print('no hay hab anterior')
        return None

    def cambio_orientacion(self):
        return self.check_orientacion() != self.hab_anterior.check_orientacion()
