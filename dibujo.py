import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from Habitacion import Habitacion
from Caja import Caja

habitaciones = []

habitaciones.append(Habitacion(0, 0, 0, 4, 4))
habitaciones[0].agregar_caja_principal(0, 0)

habitaciones.append(Habitacion(3, 0, 4, 4, 4, habitaciones[0]))
habitaciones.append(Habitacion(2, 0, 8, 4, 4, habitaciones[1]))

habitaciones.append(Habitacion(0, 4, 0, 2, 4, habitaciones[0]))
habitaciones.append(Habitacion(1, 6, 0, 4, 4, habitaciones[3]))
habitaciones.append(Habitacion(2, 10, 0, 4, 4, habitaciones[4]))

habitaciones.append(Habitacion(4, 10, 4, 4, 4, habitaciones[5]))
habitaciones.append(Habitacion(2, 10, 8, 4, 4, habitaciones[6]))

'''
==========================================
'''


# plt.figure(figsize=(20, 10))
np.linspace(0, 2, 100)
fig = plt.figure()
# fig, ax = plt.subplots(1, gridspec_kw={'width_ratios': [3]})
ax = fig.add_subplot(1, 1, 1)
# fig = plt.figure(figsize=(5,5))

major_ticks = np.arange(0, 20, 5)
minor_ticks = np.arange(0, 20, 5)

ax.set_ylim(ax.get_ylim()[::-1])
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)


for habitacion in habitaciones:
    hab_args = [(habitacion.x, habitacion.y), habitacion.ancho, habitacion.alto]
    rect = patches.Rectangle(*hab_args, linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    for caja in habitacion.cajas:
        pos_caja = [caja.x, caja.y]

        for i in range(len(pos_caja)):
            if pos_caja[i] > 0:
                pos_caja[i] -= 1

        caja_args = [(habitacion.x + pos_caja[0], habitacion.y + pos_caja[1]), 1, 1]

        print(f'caja pos {caja_args[0]}')
        rect = patches.Rectangle(*caja_args)
        ax.add_patch(rect)


# arr = [
#     [(10, 0), 10, 10],
#     [(30, 0), 10, 10],
#     [(0.6, 0.1), 0.4, 0.5]
# ]

# for i in arr:
#     rect = patches.Rectangle(*i)
#     ax.add_patch(rect)

# for i in range(1,9):
#     rect = patches.Rectangle((i*10, 50), 10, 10, linewidth=1, edgecolor='r', facecolor='none')
#     ax.add_patch(rect)
#     rect = patches.Rectangle((i*10, 50), 4, 4, linewidth=1, edgecolor='r', facecolor='none')
#     ax.add_patch(rect)

# rect = patches.Rectangle((0.1, 0.1), 0.5, 0.5, linewidth=1, edgecolor='r', facecolor='none')
# ax.add_patch(rect)

plt.show()

