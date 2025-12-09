# -*- coding: utf-8 -*-
"""
This module defines a Cell class for Conway's Game of Life, which includes the
state attribute and functionalities to compute and update the cell's state
"""

class Cell:
    """ Class representing a cell. It includes the state attribute and updates
    functionnalities.
    """

    def __init__(self, initial_state: int) -> None:
        """Initialize the state of the cell

        Parameters
        ----------
        initial_state : int
            initial state of the cell (0 or 1)

        Raises
        ------
        ValueError
            If the initial state is not 0 or 1.
        """
        if initial_state not in [0, 1]:
            raise ValueError("Cell state must be 0 or 1.")
        self.state = initial_state

    def compute_next_state(self, neighbors: list) -> int:
        """Compute the next state of the cell based on its neighbors.

        Parameters
        ----------
        neighbors : list[int]
            The states of the neighboring cells.

        Returns
        -------
        int
            The next state of the cell.
        """
        if sum(neighbors) < 2:
            return 0
        elif sum(neighbors) == 2:
            return self.state
        elif sum(neighbors) == 3:
            return 1
        else:
            return 0

    def update_state(self, new_state: int) -> None:
        """Update the state of the cell.
        Parameters
        ----------
        new_state : int
            The new state to be assigned to the cell.
        """

        self.state = new_state

    def update_cell(self, neighbors: list[int]) -> None:
        """Update the cell state based on its neighbors.
        Parameters
        ----------
        neighbors : list[int]
            The states of the neighboring cells.
        """

        new_state = self.compute_next_state(neighbors)
        self.update_state(new_state)
