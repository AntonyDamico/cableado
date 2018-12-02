from Habitacion import Habitacion
from Caja import Caja
import dibujar

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

'''
=============================================================
DISTANCIA DE LA CAJA DE LA ÚLTIMA HABITACIÓN A LA PRINCIPAL
DEBERÍA DAR 22 COMO EN LA FOTO
=============================================================
'''

caja_hab7 = hab7.cajas[-1]
print('La distancia de la caja de la habitacion 7 a la principal es:', caja_hab7.distancia_a_principal)

'''
======
FIN
======
'''

habs = [hab0, hab1, hab2, hab3, hab4, hab5, hab6, hab7]

# print(f'{hab4} {hab4.cajas[-1]}')
# print(f'{hab5} {hab5.cajas[-1]} len {len(hab5.cajas)}')
# print(f'{hab6} {hab6.cajas[-1]}\n\n')

# principal
hab0 = Habitacion(0, 8, 8, 4, 4)
hab0.agregar_caja_principal(4, 4)

# Principal - Verticales
hab1 = Habitacion(1, 8, 4, 4, 4, hab0)
hab2 = Habitacion(1, 8, 0, 4, 4, hab1)

# Principal - Verticales - Horizontal
hab3 = Habitacion(1, 4, 0, 4, 4, hab2)

# print(f'{hab1} {hab1.cajas[-1]}')
# print(f'{hab2} {hab2.cajas[-1]} len {len(hab5.cajas)}')
# print(f'{hab3} {hab3.cajas[-1]}\n')




dibujar.dibujar(habs)