from Caja import Caja
from CajaConstructor import CajaConstructor


class Habitacion:
    def __init__(self, computadoras, x, y, ancho, alto, hab_anterior=None):
        '''
        Constructor
        -------------
        args
        int computadoras: número de computadoras en la habitación
        int x: posición en x de la habitación en el plano
        int y: posición en y de la habitación en el plano
        int ancho: valor del tamaño horizontal de la habitación
        int alto: valor del tamaño vertical de la habitación
        Habitacion hab_anterior: objeto Habitación al que está conectado la habitación actual
        '''
        self.computadoras = computadoras
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        # Las cajas de la habitación van a estar guardadas en este array
        self.cajas = []
        # Determina si la habitación actual es principal
        self.principal = False
        self.hab_anterior = hab_anterior

        if hab_anterior is not None:
            # si la habitación anterior no es principal y se cambió la horientación
            if not hab_anterior.principal and self.cambio_orientacion():
                # se agrega una segunda caja a la habitación anterior
                self.hab_anterior.agregar_caja()
            # agregando caja a la habitación actual
            self.agregar_caja()

    def agregar_caja_principal(self, x, y):
        '''
        Método para agregar una caja a la habitación principal
        los argumentos van a ser la posición de esa caja
        '''
        self.principal = True
        caja_principal = Caja(x, y, self)
        self.cajas.append(caja_principal)

    '''
    ========================
    ||  Métodos privados  ||
    ========================
    '''

    def agregar_caja(self):
        '''
        Agrega un objeto caja nuevo al array de cajas
        '''
        constructor_cajas = CajaConstructor(self)
        nueva_caja = constructor_cajas.get_caja()
        self.cajas.append(nueva_caja)

    def check_orientacion(self):
        '''
        Devuelve la orientación con la que venían 
        las habitaciones puede ser horizontal o vertical
        '''
        if self.hab_anterior is not None:
            if self.hab_anterior.x != self.x:
                return 'horizontal'
            if self.hab_anterior.y != self.y:
                return 'vertical'
        print('no hay hab anterior')
        return None

    def cambio_orientacion(self):
        '''
        Devuelve un boolean que indica si la orientación ha cambiado o no
        '''
        return self.check_orientacion() != self.hab_anterior.check_orientacion()

    def __str__(self):
        return f'habitacion en posición X:{self.x} Y:{self.y}'
