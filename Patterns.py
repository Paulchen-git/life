# -*- coding: utf-8 -*-
"""
This module defines known patterns for Conway's Game of Life, along with utility
functions to register patterns, generate random grids, and load specific
patterns into a grid.
"""

from dataclasses import dataclass
from typing import Type

import numpy as np

from Cell import Cell

AVAILABLE_PATTERNS = {}


@dataclass
class Pattern:
    """This dataclass is used to store known patterns of the game of life."""
    name: str
    live_cells: list[tuple]


def register_pattern(cls: Type[Pattern]) -> Type[Pattern]:
    """
    Decorator function used to provide an up-to-date dictionary of available 
    patterns when importing the module by registering the Pattern subclasses 
    that are decorated.

    Parameters
    ----------
    cls : Type[Pattern]
        The subclass of Pattern to register.

    Returns
    -------
    Type[Pattern]
        Return the instance of the class that has been registered.
    """

    AVAILABLE_PATTERNS[cls.name] = cls

    return cls


def random_grid(length: int, width: int) -> np.ndarray:
    """Generate a random grid of cells with the provided dimensions.

    Parameters
    ----------
    length : int
        The number of columns in the grid.
    width : int
        The number of rows in the grid.

    Returns
    -------
    np.ndarray
        A grid of Cell objects with random initial states.
    """
    grid = np.empty((width, length), dtype=object)
    for i in range(width):
        for j in range(length):
            grid[i][j] = Cell(initial_state=np.random.choice([0, 1]))

    return grid

def load_pattern(pattern: Type[Pattern], length: int, width: int) -> np.ndarray:
    """Load a given pattern in the top-left corner of a grid of dimensions 
    (width, length).

    Parameters
    ----------
    pattern : Type[Pattern]
        The pattern to be loaded
    length : int
        The number of columns in the grid
    width : int
        The number of rows in the grid

    Returns
    -------
    np.ndarray
        A grid of Cell object containing the provided pattern.
    """
    grid = np.empty((width, length), dtype=object)
    for i in range(width):
        for j in range(length):
            grid[i][j] = Cell(initial_state=0)
    for x, y in pattern.live_cells:
        if x < width and y < length:
            grid[x][y].state = 1
    return grid

@register_pattern
class BLOCK(Pattern):
    """A simple 2x2 block pattern that remains stable over generations."""
    name = 'block'
    live_cells = [
        (1, 1), (1, 2),
        (2, 1), (2, 2)
    ]

@register_pattern
class BLINKER(Pattern):
    """A simple oscillator pattern that alternates between vertical and 
    horizontal states."""
    name = 'blinker'
    live_cells = [
        (1, 0),
        (1, 1),
        (1, 2)
    ]

@register_pattern
class PULSAR(Pattern):
    """A larger oscillator pattern with a period of 3 generations."""
    name = 'pulsar'
    live_cells = [
        (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
        (4, 2), (5, 2), (6, 2), (4, 7), (5, 7), (6, 7),
        (4, 9), (5, 9), (6, 9), (4, 14), (5, 14), (6, 14),
        (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
        (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
        (10, 2), (11, 2), (12, 2), (10, 7), (11, 7), (12, 7),
        (10, 9), (11, 9), (12, 9), (10, 14), (11, 14), (12, 14),
        (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)
    ]

@register_pattern
class GLIDER(Pattern):
    """A small pattern that moves diagonally across the grid over generations.
    """
    name = 'glider'
    live_cells = [
        (0, 1),
        (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

@register_pattern
class GOSPER_GLIDER_GUN(Pattern):
    """A complex pattern that periodically emits gliders."""
    name = 'glider_gun'
    live_cells = [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (5, 11), (6, 11), (7, 11),
        (4, 12), (8, 12),
        (3, 13), (9, 13),
        (3, 14), (9, 14),
        (6, 15),
        (4, 16), (8, 16),
        (5, 17), (6, 17), (7, 17),
        (6, 18),
        (3, 21), (4, 21), (5, 21),
        (3, 22), (4, 22), (5, 22),
        (2, 23), (6, 23),
        (1, 25), (2, 25), (6, 25), (7, 25),
        (3, 35), (4, 35),
        (3, 36), (4, 36)
    ]
