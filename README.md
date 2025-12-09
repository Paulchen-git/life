# Conway's Game of Life

This repository provides a modular and extensible implementation of Conway's Game of Life in Python, featuring:
- Customizable grid size and initial patterns
- Pattern registration and management
- Visualization and animation
- Entropy computation
- Unit tests for all core modules

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It consists of a grid of cells that evolve through generations according to simple rules based on the states of neighboring cells. This project allows you to simulate, visualize, and analyze the Game of Life with various initial patterns.

## Features

- **Grid and Cell Classes**: Core logic for cell state updates and grid management
- **Pattern System**: Easily add and use named patterns (e.g., block, blinker, glider, pulsar, Gosper glider gun)
- **Visualization**: Display and animate the grid using matplotlib
- **Entropy Analysis**: Track the entropy of the grid over time
- **Unit Tests**: Comprehensive tests for reliability

## Installation

1. Clone the repository:
	```bash
	git clone https://github.com/Paulchen-git/life.git
	cd life
	```
2. (Optional) Create and activate a Python virtual environment using Conda:
	```bash
	conda create -n life_env python=3.10
	conda activate life_env
	```
3. Install required packages:
	```bash
    conda install numpy matplotlib
	```

## Usage

### Run a Simulation

You can run a simulation and save an animation as a GIF:

```bash
python run_simulation.py
```

This will use the default grid size and pattern. You can modify `run_simulation.py` to select a different pattern or grid size.

### Using Patterns

Patterns are defined in `Patterns.py` and registered automatically. Available patterns include:

- `block`
- `blinker`
- `glider`
- `pulsar`
- `glider_gun`

To start with a specific pattern:

```python
from Grid import Grid
grid = Grid(length=64, width=64, pattern='glider')
```

Or use a custom pattern:

```python
from Patterns import Pattern
custom = Pattern(name='my_pattern', live_cells=[(0,0), (1,1)])
grid = Grid(length=10, width=10, pattern=custom)
```

### Visualization

You can visualize the grid and its evolution using matplotlib. See `notebook.ipynb` for interactive analysis and entropy tracking.

### Entropy Analysis

The `compute_entropy` function in `utils.py` computes the entropy of the grid, useful for analyzing the system's evolution.

### Boundary Conditions
The grid supports various boundary conditions:
- `fixed`: Cells outside the grid are always dead.
- `periodic`: The grid wraps around (toroidal).
- `reflective`: Edges reflect the state of the nearest cell.

## Testing

Run all unit tests with:

```bash
python tests.py
```

## Extending Patterns

To add a new pattern, define a new class in `Patterns.py` and decorate it with `@register_pattern`:

```python
@register_pattern
class MY_PATTERN(Pattern):
	 name = 'my_pattern'
	 live_cells = [(0,0), (1,1), (2,2)]
```

## Project Structure

- `Cell.py` — Cell logic
- `Grid.py` — Grid management and visualization
- `Patterns.py` — Pattern definitions and registration
- `utils.py` — Utility functions (e.g., entropy)
- `run_simulation.py` — Example simulation script
- `tests.py` — Unit tests
- `notebook.ipynb` — Interactive analysis
