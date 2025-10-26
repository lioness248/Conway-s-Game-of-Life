import numpy as np
import os
import time

world = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

def count_neighbors(expanded_grid, row, col):
    area = expanded_grid[row-1:row+2, col-1:col+2]
    return np.sum(area) - expanded_grid[row, col]

def evolve(grid):
    expanded = np.pad(grid, 1, mode="constant")
    next_grid = np.zeros_like(grid)

    for r in range(1, expanded.shape[0] - 1):
        for c in range(1, expanded.shape[1] - 1):
            alive_neighbors = count_neighbors(expanded, r, c)
            cell_state = expanded[r, c]

            if cell_state == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                next_grid[r-1, c-1] = 1
            elif cell_state == 0 and alive_neighbors == 3:
                next_grid[r-1, c-1] = 1
            else:
                next_grid[r-1, c-1] = 0

    return next_grid

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(world)
    world = evolve(world)
    time.sleep(1)
