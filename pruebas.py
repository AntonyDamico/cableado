from Habitacion import Habitacion
from Caja import Caja
import dibujar

habitaciones = []

habitaciones.append(Habitacion(0, 0, 0, 4, 4))
habitaciones[0].agregar_caja_principal(0, 4)

habitaciones.append(Habitacion(0,4,0,4,4, habitaciones[0]))
habitaciones.append(Habitacion(0, 4,4,4,4,habitaciones[1]))

dibujar.dibujar_plano(habitaciones)
