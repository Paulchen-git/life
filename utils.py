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