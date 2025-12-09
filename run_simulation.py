# -*- coding: utf-8 -*-
"""
This script runs a simulation of Conway's Game of Life using the Grid class
and visualizes the evolution of the grid over a number of epochs, saving the
resulting animation as a GIF file.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation, rc

from Cell import Cell
from Grid import Grid

if __name__ == "__main__":
    grid = Grid(length=64, width=64, seed=42)
    fig, ax = plt.subplots()
    ims = []
    for _ in range(10):
        grid.update_grid()
        im = grid.display_grid(ax=ax)
        ims.append([im])
    # Add the varying number of epochs in the animation
    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)

    ani.save('game_of_life_simulation.gif', writer='pillow')
    plt.show()