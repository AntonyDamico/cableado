from Habitacion import Habitacion
from Caja import Caja
from Arbol import Arbol

hab0 = Habitacion(0, 0, 0, 4, 4)
hab0.agregar_caja_principal(0, 0)

hab1 = Habitacion(2, 0, 4, 4, 4, hab0)
hab2 = Habitacion(1, 4, 0, 2, 4, hab0)
hab3 = Habitacion(2, 4, 4, 2, 4, hab2)
