from estructura.Habitacion import Habitacion
from plano import plano

habitaciones = []

habitaciones.append(Habitacion(0, 0, 0, 4, 4))
habitaciones[0].agregar_caja_principal(0, 4)

habitaciones.append(Habitacion(0,4,0,4,4, habitaciones[0]))
habitaciones.append(Habitacion(0, 4,4,4,4,habitaciones[1]))

plano.dibujar(habitaciones)
