from Caja import Caja

class CajaConstructor:

    def __init__(self, habitacion):
        self.habitacion = habitacion

    def get_caja(self):
        '''
        Devuele un nuevo objeto Caja
        si es la única en la habitación usa el mismo x & y de la anterior
        si es la segunda, se mueve según sea la orientación anterior
        '''
        # última caja de la habitación anterior
        caja_anterior = self.habitacion.hab_anterior.cajas[-1]
        new_x = caja_anterior.x
        new_y = caja_anterior.y
        habitacion_nueva_caja = self.habitacion

        # cambiando los x & y de la caja si ya existe una en la habitación
        if self.habitacion.cajas:
            caja_anterior = self.habitacion.cajas[0]
            if self.habitacion.check_orientacion() == 'horizontal':
                new_x = self.get_nueva_posicion(caja_anterior.x, self.habitacion.ancho)
            if self.habitacion.check_orientacion() == 'vertical':
                new_y = self.get_nueva_posicion(caja_anterior.y, self.habitacion.alto)

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

