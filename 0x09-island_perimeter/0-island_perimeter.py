#!/usr/bin/python3

"""
Title: Island Perimeter
Description: Create a function def island_perimeter(grid): that returns the
perimeter of the island described in grid:
- grid is a list of list of integers:
- - 0 represents water
- - 1 represents land
- - Each cell is square, with a side length of 1
- - Cells are connected horizontally/vertically (not diagonally).
- - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected
to the water surrounding the island)
"""


def island_perimeter(grid):
    """ fxn that returns the perimeter of the island """

    # initialize the perimeter
    perimeter = 0

    for x1 in range(len(grid)):

        for x2 in range(len(grid[x1])):

            if (grid[x1][x2] == 1):

                if (x1 <= 0 or grid[x1 - 1][x2] == 0):
                    perimeter = perimeter + 1
                if (x1 >= len(grid) - 1 or grid[x1 + 1][x2] == 0):
                    perimeter = perimeter + 1
                if (x2 <= 0 or grid[x1][x2 - 1] == 0):
                    perimeter = perimeter + 1
                if (x2 >= len(grid[x1]) - 1 or grid[x1][x2 + 1] == 0):
                    perimeter = perimeter + 1

    return perimeter
