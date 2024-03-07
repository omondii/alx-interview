#!/usr/bin/python3
""" A func to calculate the perimeter of a grid
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
"""


def island_perimeter(grid):
    """ Find perimeter from a list """
    island_size = sum([i for list in grid for i in list])
    perimeter = island_size * 2 + 2

    # correct for inner tiles
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            if (grid[i][j] == 1 and grid[i+1][j] == 1
                    and grid[i][j+1] == 1 and grid[i+1][j+1] == 1):
                perimeter -= 2

    return perimeter
