#!/usr/bin/python3

"""
Title: N queens
Description: The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem
Author: @a_idk
"""

import sys


# Checking if only one argument for N should be given
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

# Verify that the provided argument is a valid int
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Ensuring that input N is at least 4
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])  # Store the input N as an int


def qn(n, i=0, a=[], b=[], c=[]):
    """ Recursive generator function to find valid queen positions """

    if i < n:
        # Loop through each column position current row to check for conflicts
        for j in range(n):
            # Checking for conflict with other queens
            if j not in a and i + j not in b and i - j not in c:
                yield from qn(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        # Yield a solution when queens are successfully placed in all rows
        yield a


def solve(n):
    """ Solve the N-Queens problem by generating all valid board configs """

    k = []
    i = 0
    for solution in qn(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
