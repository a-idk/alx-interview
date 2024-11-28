#!/usr/bin/python3
"""
Title: Changes comes from within
Description: determine the fewest number of coins needed to meet a given
amount total
"""


def makeChange(coins, total):
    """ fxn that fewest number of coins needed to meet total """

    # check if total is 0 or less
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()

        count = 0

        for x in coin:
            while(total >= x):
                count = count + 1
                total = total - x

        if total == 0:
            return count

        return -1
