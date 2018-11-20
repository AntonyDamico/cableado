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
        caja_principal = Caja(x, y)
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
        nueva_caja = self.crear_caja()
        self.cajas.append(nueva_caja)

    def crear_caja(self):
        '''
        Devuele un nuevo objeto Caja
        si es la única en la habitación usa el mismo x & y de la anterior
        si es la segunda, se mueve según sea la orientación anterior
        '''
        # última caja de la habitación anterior
        caja_anterior = self.hab_anterior.cajas[-1]
        new_x = caja_anterior.x
        new_y = caja_anterior.y

        # cambiando los x & y de la caja si ya existe una en la habitación
        if self.cajas:
            if self.check_orientacion() == 'horizontal':
                new_x = caja_anterior.x + self.ancho
            if self.check_orientacion() == 'vertical':
                new_y = caja_anterior.y + self.alto

        return Caja(new_x, new_y, caja_anterior)

    def check_orientacion(self):
        '''
        Devuelve la orientación con la que venían las cajas
        puede ser horizontal o vertical
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
