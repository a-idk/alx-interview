#!/usr/bin/python3
"""
Title: Minimum Operations
Description: write a method that calculates the fewest number of operations
"""


def minOperations(n):
    """ minimum operations """

    # if n is just 1 or less
    if (n < 2):
        return 0

    outcome = 0
    x = 2  # this is the root

    while x <= n:
        if n % x == 0:  # even division
            outcome = outcome + x
            n = n / x  # set n to the remainder
            x = x - 1  # reduce x to get smaller value
        # to exit the loop
        x = x + 1

    return outcome
