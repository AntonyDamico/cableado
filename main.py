from Habitacion import Habitacion
from Caja import Caja
from Arbol import Arbol

# habitación principal
hab0 = Habitacion(0, 0, 0, 4, 4)
hab0.agregar_caja_principal(0, 0)

# Principal - Verticales
hab1 = Habitacion(3, 0, 4, 4, 4, hab0)
hab2 = Habitacion(2, 0, 8, 4, 4, hab1)

# Principal - Horizontales
hab3 = Habitacion(0, 4, 0, 2, 4, hab0)
hab4 = Habitacion(1, 6, 0, 4, 4, hab3)
hab5 = Habitacion(2, 10, 0, 4, 4, hab4)

# Principal - Horizontales - Verticales
hab6 = Habitacion(4, 10, 4, 4, 4, hab5)
hab7 = Habitacion(2, 10, 8, 4, 4, hab6)
