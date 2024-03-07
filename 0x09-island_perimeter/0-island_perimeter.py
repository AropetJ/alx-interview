#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """A function that returns the perimeter of the island described in grid

    Args:
        grid: a list of list of integers
    Returns:
        perimeter: an integer
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
