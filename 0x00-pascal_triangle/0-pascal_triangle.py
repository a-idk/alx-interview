#!/usr/bin/python3
"""
Description: Code to print out pascal triangle
Author: @a_idk
"""


def pascal_triangle(n):
    """
    Function that returns a list of list of integers
    representing the Pascal Triangle
    n = integer
    """
    if n <= 0:  # n will always be an interger
        return []

    tri = [[1]]
    # list
    for row_idx in range(1, n):
        row = [1]
        # list of lists
        for x in range(1, row_idx):
            # implementing the pascal triangle relationship
            elem = tri[row_idx - 1][x - 1] + tri[row_idx - 1][x]
            row.append(elem)
        row.append(1)
        tri.append(row)
    return tri
