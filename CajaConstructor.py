from Caja import Caja


class CajaConstructor:
    def __init__(self, habitacion):
        self.habitacion = habitacion

    def get_caja(self):
        '''
        Devuele un nuevo objeto Caja con
        la posicion adecuada
        '''
        caja_anterior = self.habitacion.hab_anterior.cajas[-1]
        habitacion_nueva_caja = self.habitacion
        new_x, new_y = self.get_posicion(caja_anterior)
        return Caja(new_x, new_y, habitacion_nueva_caja, caja_anterior)

    def get_posicion(self, caja_anterior):
        '''
        Devuelve la posicion de la caja que va a ser agregada
        si es la única en la habitación usa el mismo x & y de la anterior
        si es la segunda, se mueve según sea la orientación anterior
        '''
        new_x = caja_anterior.x
        new_y = caja_anterior.y

        if self.habitacion.cajas:
            caja_anterior = self.habitacion.cajas[0]
            if self.habitacion.check_orientacion() == 'horizontal':
                new_x = self.get_nueva_posicion(
                    caja_anterior.x, self.habitacion.ancho)
            if self.habitacion.check_orientacion() == 'vertical':
                new_y = self.get_nueva_posicion(
                    caja_anterior.y, self.habitacion.alto)

        return new_x, new_y

    def get_nueva_posicion(self, caja_anterior_pos, distancia):
        '''
        Devuelve una nueva posición para una segunda caja en la habitación
        Si la primera estaba en 0, la empuja hacia la siguiente pared
        Si no los estaba, lo devuelve a la pared que sea 0
        '''
        if caja_anterior_pos == 0:
            return caja_anterior_pos + distancia
        return 0
