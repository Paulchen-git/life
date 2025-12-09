# -*- coding: utf-8 -*-
"""
This module defines the Grid class for Conway's Game of Life, which manages
the grid of cells, their initialization, updating, and visualization.
"""

from typing import Type

import matplotlib.pyplot as plt
import numpy as np

from Patterns import AVAILABLE_PATTERNS, Pattern, load_pattern, random_grid
from utils import get_neighbors

class Grid:
    """Class representing the grid for Conway's Game of Life.
    """

    def __init__(
            self, 
            length: int, 
            width: int, 
            seed: int=42, 
            boundary_conditions: str="periodic",
            pattern: Type[Pattern]=None
    ) -> None:
        """Initialize the grid with given dimensions, random seed, and optional
        pattern.

        Parameters
        ----------
        length : int
            The number of columns in the grid.
        width : int
            The number of rows in the grid.
        seed : int, optional
            The random seed for reproductibility, by default 42
        boundary_conditions : str, optional
            The type of boundary conditions to apply ("fixed", "periodic", 
            "reflective", "toroidal"), by default "periodic"
        pattern : Type[Pattern], optional
            The pattern to be used to initialize the grid, by default None 
            (random grid)
        """

        self.length = length
        self.width = width
        self.seed = seed
        self.boundary_conditions = boundary_conditions
        np.random.seed(self.seed)
        self.__initialize_grid(pattern)


    def __initialize_grid(self, pattern: Type[Pattern]=None) -> None:
        """Initialize randomly or with a given pattern the grid by filling it 
        with Cell objects.

        Parameters
        ----------
        pattern : Type[Pattern], optional
            The pattern used to initialize the grid, by default None

        Raises
        ------
        ValueError
            Raises an error if provided pattern doesn't exist or isn't a Pattern
            instance.
        """

        if isinstance(pattern, Pattern):
            self.grid = load_pattern(pattern, self.length, self.width)
        elif pattern in AVAILABLE_PATTERNS:
            self.grid = load_pattern(
                AVAILABLE_PATTERNS[pattern],
                self.length, 
                self.width
            )
        elif pattern is None:
            self.grid = random_grid(self.length, self.width)
        else:
            raise ValueError("Invalid pattern specified. Must be a Pattern " \
            "instance or a valid pattern name. List of available patterns: " +
            ", ".join(AVAILABLE_PATTERNS.keys()))


    def display_grid(self, ax) -> plt.imshow:
        """Create a grid of int corresponding to the cell states in order to 
        plot the grid. 

        Parameters (TODO -> this function should be modified)
        ----------
        ax : _type_
            _description_

        Returns
        -------
        _type_
            _description_
        """

        display_array = np.zeros((self.width, self.length))
        for i in range(self.width):
            for j in range(self.length):
                display_array[i][j] = self.grid[i][j].state
        im = ax.imshow(display_array, cmap='binary', animated=True)
        return im
    

    def get_grid(self) -> np.ndarray:
        """Get all the states from the grid of cells to return a grid of state.

        Returns
        -------
        np.ndarray
            The grid in an array of ints (states).
        """

        return np.array(
            [[self.grid[i][j].state for j in range(self.length)] 
             for i in range(self.width)]
        )


    def save_grid(self, filepath: str="fig/grid_saved.png"):
        """Save a plot of the current grid.

        Parameters
        ----------
        filepath : str
            The path where we save the figure.
        """

        display_array = np.zeros((self.width, self.length))
        for i in range(self.width):
            for j in range(self.length):
                display_array[i][j] = self.grid[i][j].state
        plt.imsave(filepath, display_array, cmap='binary')


    def update_grid(self) -> None:
        """Update the grid by updating the state of every cells."""

        new_states = np.zeros((self.width, self.length))
        for i in range(self.width):
            for j in range(self.length):
                neighbors = get_neighbors(self, i, j)
                new_states[i][j] = self.grid[i][j].compute_next_state(neighbors)
        for i in range(self.width):
            for j in range(self.length):
                self.grid[i][j].update_state(new_states[i][j])
