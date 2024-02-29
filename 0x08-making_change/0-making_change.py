#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    """A function that determines the fewest number of coins needed to meet a
    given amount total. If the total is 0 or less, the function should return
    0. If the total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    for coin in sorted_coins:
        if total // coin > 0:
            coins_count += total // coin
            total %= coin
    if total != 0:
        return -1
    return coins_count
