#!/usr/bin/python3
"""
This module provides a function to calculate the perimeter of an island
in a rectangular grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A rectangular grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell starts with 4 sides
                perimeter += 4

                # Check if there's an adjacent land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check if there's an adjacent land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
