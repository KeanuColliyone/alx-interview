#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.

Functions:
    makeChange(coins, total): Returns the fewest number of coins needed or -1.
"""


from functools import lru_cache


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): The values of the coins in your possession.
        total (int): The target amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    @lru_cache(maxsize=None)
    def dp(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        return min(dp(amount - coin) + 1 for coin in coins)

    result = dp(total)
    return result if result != float('inf') else -1
