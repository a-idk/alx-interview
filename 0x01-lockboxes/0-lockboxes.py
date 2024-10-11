#!/usr/bin/python3
"""
TItle: Lock Boxes
Author: @a_Idk
"""


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened """
    # Variables definition and declaration
    n = len(boxes)  # total number of boxes
    keys = [0]
    c = 0
    i = 0

    while i < len(keys):
        current_box = keys[i]

        for key in boxes[current_box]:
            # check if key opens a valid box and if not collected already
            if 0 < key < n and key not in keys:
                keys.append(key)
                c = c + 1
        i = i + 1
    return c == n - 1
