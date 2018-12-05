from estructura.Habitacion import Habitacion
from plano import plano

habitaciones = []

# habitación principal
habitaciones.append(Habitacion(0, 0, 0, 4, 4))
habitaciones[0].agregar_caja_principal(0, 0)

# Principal - Verticales
habitaciones.append(Habitacion(3, 0, 4, 4, 4, habitaciones[0]))
habitaciones.append(Habitacion(2, 0, 8, 4, 4, habitaciones[1]))

# Principal - Horizontales
habitaciones.append(Habitacion(0, 4, 0, 2, 4, habitaciones[0]))
habitaciones.append(Habitacion(1, 6, 0, 4, 4, habitaciones[3]))
habitaciones.append(Habitacion(2, 10, 0, 4, 4, habitaciones[4]))

# Principal - Horizontales - Verticales
habitaciones.append(Habitacion(4, 10, 4, 4, 4, habitaciones[5]))
habitaciones.append(Habitacion(2, 10, 8, 4, 4, habitaciones[6]))

'''
=============================================================
CALCULO DE LA CANTIDAD DE METROS DE CABLE NECESARIOS
=============================================================
'''

cableado_aereo = sum([hab.cableado_aereo for hab in habitaciones])
cableado_bajada = sum([hab.cableado_bajada for hab in habitaciones])

error = 0.12

margen_de_error = error * (cableado_aereo+cableado_bajada)

cable_piso = cableado_aereo + cableado_bajada + margen_de_error

pisos = 2

cable_edificio = cable_piso * pisos

precio_mt = 15

precio_total = precio_mt * cable_edificio

print('aereo:', cableado_aereo, 'bajada:',cableado_bajada)
print('margen de error: ', margen_de_error)
print('costo piso:', cable_piso)
print('costo edificio de', pisos, 'pisos:', cable_edificio)
print('precio para el edificio a', precio_mt, 'por metro:', precio_total)

plano.dibujar(habitaciones)


'''
=============================================================
DISTANCIA DE LA CAJA DE LA ÚLTIMA HABITACIÓN A LA PRINCIPAL
DEBERÍA DAR 22 COMO EN LA FOTO
=============================================================
'''

# caja_hab7 = habitaciones[7].cajas[-1]
# print('La distancia de la caja de la habitacion 7 a la principal es:',
#       caja_hab7.distancia_a_principal)

# print('cableado aereo:', habitaciones[7].cableado_aereo)
# print('cableado bajadas:', habitaciones[7].cableado_bajada)
'''
======
FIN
======
'''

# habs = [hab0, hab1, hab2, hab3, hab4, hab5, hab6, hab7]

# print(f'{hab4} {hab4.cajas[-1]}')
# print(f'{hab5} {hab5.cajas[-1]} len {len(hab5.cajas)}')
# print(f'{hab6} {hab6.cajas[-1]}\n\n')

# principal
# hab0 = Habitacion(0, 8, 8, 4, 4)
# hab0.agregar_caja_principal(4, 4)

# Principal - Verticales
# hab1 = Habitacion(1, 8, 4, 4, 4, hab0)
# hab2 = Habitacion(1, 8, 0, 4, 4, hab1)

# Principal - Verticales - Horizontal
# hab3 = Habitacion(1, 4, 0, 4, 4, hab2)

# print(f'{hab1} {hab1.cajas[-1]}')
# print(f'{hab2} {hab2.cajas[-1]} len {len(hab5.cajas)}')
# print(f'{hab3} {hab3.cajas[-1]}\n')
