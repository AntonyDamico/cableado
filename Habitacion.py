from Caja import Caja


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
        habitacion_nueva_caja = self

        # cambiando los x & y de la caja si ya existe una en la habitación
        if self.cajas:
            caja_anterior = self.cajas[0]
            if self.check_orientacion() == 'horizontal':
                new_x = self.get_nueva_posicion(caja_anterior.x, self.ancho)
            if self.check_orientacion() == 'vertical':
                new_y = self.get_nueva_posicion(caja_anterior.y, self.alto)

        return Caja(new_x, new_y, habitacion_nueva_caja, caja_anterior)


    def get_nueva_posicion(self, caja_anterior_pos, distancia):
        '''
        Devuelve una nueva posición para una segunda caja en la habitación
        Si la primera estaba en 0, la empuja hacia la siguiente pared
        Si no los estaba, lo devuelve a la pared que sea 0
        '''
        if caja_anterior_pos == 0:
            return caja_anterior_pos + distancia
        return 0


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

    def __str__(self):
        return f'habitacion en posición X:{self.x} Y:{self.y}'