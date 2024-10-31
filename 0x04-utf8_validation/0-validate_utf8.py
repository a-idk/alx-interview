#!/usr/bin/python3
"""
Title: UTF-8 Validation
Description: Write a method that determines if a given data set represents
a valid UTF-8 encoding
Author: @a_Idk
"""


def leading_set(num):
    """ mthd that returns the leading set bits """

    # assign values to variables
    fix_dbits = 0
    x = 1 << 7  # assigning 128 to variable

    while x & num:
        fix_dbits = fix_dbits + 1
        x = x >> 1  # shifting the bits to the right

    return fix_dbits


def validUTF8(data):
    """
    mthd that determines if a given data set represents a valid UTF-8 encoding
    """

    # intializing the bit count
    c = 0

    for num in range(len(data)):
        if c == 0:
            c = leading_set(data[num])

            if c == 0:
                continue

            # checking for 1 to 4 bytes
            if c == 1 or c > 4:
                return False
        else:
            # format checks
            if not (data[num] & (1 << 7) and not (data[num] & (1 << 6))):
                return False

        c = c - 1
    return c == 0
