#!/usr/bin/python3
def island_perimeter(grid):
    island_size = sum([i for l in grid for i in l])
    perimeter = island_size * 2 + 2

    # correct for inner tiles
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            if (grid[i][j] == 1 and grid[i+1][j] == 1 
                    and grid[i][j+1] == 1 and grid[i+1][j+1] == 1):
                perimeter -= 2

    return perimeter
