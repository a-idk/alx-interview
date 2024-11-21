#!/usr/bin/python3

"""
Title: Rotate 2D Matrix
Description: Given an n x n 2D matrix rotate it 90 degrees clockwise.
-   Prototype: def rotate_2d_matrix(matrix):
-   Do not return anything. The matrix must be edited in-place.
-   You can assume the matrix will have 2 dimensions and will not be empty
"""


def rotate_2d_matrix(matrix):
    """ method that rotates a 2D Matrix """
    # declaring variable
    num = len(matrix)

    for x in range(num):
        for y in range(x, num):
            matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
    for x in range(num):
        matrix[x] = matrix[x][::-1]
