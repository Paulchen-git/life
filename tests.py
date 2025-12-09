# -*- coding: utf-8 -*-
"""
This module contains unit tests for the Cell, Grid, and Patterns modules of
Conway's Game of Life implementation.
"""

import os
import unittest

import matplotlib.pyplot as plt
import numpy as np

from Cell import Cell
from Grid import Grid
from Patterns import AVAILABLE_PATTERNS, Pattern, load_pattern, random_grid
from utils import compute_entropy


class TestCell(unittest.TestCase):
	def test_initialization(self):
		cell0 = Cell(0)
		cell1 = Cell(1)
		self.assertEqual(cell0.state, 0)
		self.assertEqual(cell1.state, 1)

	def test_compute_next_state(self):
		cell = Cell(1)
		# Underpopulation
		self.assertEqual(cell.compute_next_state([0, 0, 0, 0, 0, 0, 0, 0]), 0)
		# Survival
		self.assertEqual(cell.compute_next_state([1, 1, 0, 0, 0, 0, 0, 0]), 1)
		# Reproduction
		cell.state = 0
		self.assertEqual(cell.compute_next_state([1, 1, 1, 0, 0, 0, 0, 0]), 1)
		# Overpopulation
		self.assertEqual(cell.compute_next_state([1, 1, 1, 1, 1, 0, 0, 0]), 0)

	def test_update_state(self):
		cell = Cell(0)
		cell.update_state(1)
		self.assertEqual(cell.state, 1)

	def test_update_cell(self):
		cell = Cell(1)
		cell.update_cell([0, 0, 0, 0, 0, 0, 0, 0])
		self.assertEqual(cell.state, 0)

class TestPatterns(unittest.TestCase):
	def test_pattern_dataclass(self):
		p = Pattern(name='test', live_cells=[(0, 0), (1, 1)])
		self.assertEqual(p.name, 'test')
		self.assertEqual(p.live_cells, [(0, 0), (1, 1)])

	def test_random_grid(self):
		grid = random_grid(5, 5)
		self.assertEqual(grid.shape, (5, 5))
		states = [grid[i][j].state for i in range(5) for j in range(5)]
		self.assertTrue(all(s in [0, 1] for s in states))

	def test_load_pattern(self):
		pattern = Pattern(name='test', live_cells=[(0, 0), (1, 1)])
		grid = load_pattern(pattern, 3, 3)
		self.assertEqual(grid[0][0].state, 1)
		self.assertEqual(grid[1][1].state, 1)
		self.assertEqual(grid[2][2].state, 0)

	def test_available_patterns(self):
		self.assertTrue('block' in AVAILABLE_PATTERNS)
		self.assertTrue('blinker' in AVAILABLE_PATTERNS)
		self.assertTrue('glider' in AVAILABLE_PATTERNS)

class TestGrid(unittest.TestCase):
	def test_init_random(self):
		grid = Grid(5, 5)
		self.assertEqual(grid.grid.shape, (5, 5))

	def test_init_pattern_str(self):
		grid = Grid(5, 5, pattern='block')
		self.assertEqual(grid.grid[1][1].state, 1)

	def test_init_pattern_instance(self):
		pattern = Pattern(name='custom', live_cells=[(0, 0)])
		grid = Grid(3, 3, pattern=pattern)
		self.assertEqual(grid.grid[0][0].state, 1)

	def test_invalid_pattern_name(self):
		with self.assertRaises(ValueError):
			Grid(5, 5, pattern='not_a_pattern')

	def test_display_grid(self):
		grid = Grid(5, 5)
		fig, ax = plt.subplots()
		im = grid.display_grid(ax)
		self.assertTrue(hasattr(im, 'get_array'))
		plt.close(fig)

	def test_get_grid(self):
		grid = Grid(3, 3, pattern='block')
		arr = grid.get_grid()
		self.assertEqual(arr.shape, (3, 3))
		self.assertEqual(arr[1][1], 1)

	def test_save_grid(self):
		grid = Grid(3, 3, pattern='block')
		filename = 'test_grid.png'
		grid.save_grid(filename)
		self.assertTrue(os.path.exists(filename))
		os.remove(filename)

	def test_update_grid(self):
		grid = Grid(3, 3, pattern='block')
		before = grid.get_grid().copy()
		grid.update_grid()
		after = grid.get_grid()
		self.assertTrue(np.array_equal(before, after))  # Block is stable

	def test_get_neighbors(self):
		grid = Grid(3, 3, pattern='block')
		neighbors = grid._Grid__get_neighbors(1, 1)
		self.assertEqual(len(neighbors), 8)

class TestUtils(unittest.TestCase):
	def test_entropy_all_dead(self):
		pattern = Pattern(name='dead', live_cells=[])
		grid = Grid(3, 3, pattern=pattern)
		entropy = compute_entropy(grid)
		self.assertEqual(entropy, 0)

	def test_entropy_all_alive(self):
		pattern = Pattern(name='alive', live_cells=[(i, j) for i in range(3) for j in range(3)])
		grid = Grid(3, 3, pattern=pattern)
		entropy = compute_entropy(grid)
		self.assertEqual(entropy, 0)

	def test_entropy_mixed(self):
		pattern = Pattern(name='mixed', live_cells=[(0, 0), (1, 1), (2, 2)])
		grid = Grid(3, 3, pattern=pattern)
		entropy = compute_entropy(grid)
		self.assertTrue(entropy > 0)

if __name__ == '__main__':
	unittest.main()
