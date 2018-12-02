import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

np.linspace(0, 2, 100)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def dibujar(habitaciones):
    setup_ticks(habitaciones[-1])

    for habitacion in habitaciones:
    # Dibujando habitación
        hab_args = [(habitacion.x, habitacion.y), habitacion.ancho, habitacion.alto]
        rect = patches.Rectangle(*hab_args, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Dibujando cajas
        for caja in habitacion.cajas:
            pos_caja = [caja.x, caja.y]

            for i in range(len(pos_caja)):
                if pos_caja[i] > 0:
                    pos_caja[i] -= 1

            caja_args = [(habitacion.x + pos_caja[0], habitacion.y + pos_caja[1]), 1, 1]
            rect = patches.Rectangle(*caja_args)
            ax.add_patch(rect)
    plt.show()


def setup_ticks(habitacion):
    max_number = max(habitacion.x, habitacion.y)
    max_number += max(habitacion.ancho, habitacion.alto)
    max_number += math.ceil(float(max_number) / 5)

    major_ticks = np.arange(0, max_number, 1)
    minor_ticks = np.arange(0, max_number, 1)

    # Dibujando los ticks
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)