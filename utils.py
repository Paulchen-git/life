# -*- coding: utf-8 -*-

import numpy as np

def compute_entropy(grid):
    """_summary_

    Parameters
    ----------
    grid : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    state_counts = {0: 0, 1: 0}
    for i in range(grid.width):
        for j in range(grid.length):
            state_counts[grid.grid[i][j].state] += 1
    total_cells = grid.width * grid.length
    entropy = 0
    for count in state_counts.values():
        if count > 0:
            probability = count / total_cells
            entropy -= probability * np.log2(probability)
    return entropy

def get_neighbors(grid, x, y):
    """Get the states of all neighbor cells of cell (x, y) with specified 
    boundary conditions.

    Parameters
    ----------
    grid : Grid
        The grid object containing the cells.
    x : int
        The x-coordinate of the cell.
    y : int
        The y-coordinate of the cell.

    Returns
    -------
    list[int]
        A list of states of the neighboring cells.
    """
    neighbors = []
    boundary_conditions = grid.boundary_conditions
    if boundary_conditions == "fixed":
        for i in range(-1, 2):
            for j in range(-1, 2):
                ni, nj = x + i, y + j
                if i == 0 and j == 0:
                    continue
                if 0 <= ni < grid.width and 0 <= nj < grid.length:
                    neighbors.append(grid.grid[ni][nj].state)
                else:
                    neighbors.append(0)  # Out of bounds treated as dead cell
        return neighbors
    elif boundary_conditions == "periodic":
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                ni, nj = (x + i) % grid.width, (y + j) % grid.length
                neighbors.append(grid.grid[ni][nj].state)
        return neighbors
    elif boundary_conditions == "reflective":
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                ni, nj = x + i, y + j
                if ni < 0:
                    ni = 0
                elif ni >= grid.width:
                    ni = grid.width - 1
                if nj < 0:
                    nj = 0
                elif nj >= grid.length:
                    nj = grid.length - 1
                neighbors.append(grid.grid[ni][nj].state)
        return neighbors
    elif boundary_conditions == "toroidal":
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                ni = (x + i) % grid.width
                nj = (y + j) % grid.length
                neighbors.append(grid.grid[ni][nj].state)
        return neighbors
    else:
        raise ValueError(f"Unknown boundary condition: {boundary_conditions}. "
                         "Supported conditions are 'fixed', 'periodic', " \
                         "'reflective', and 'toroidal'.")