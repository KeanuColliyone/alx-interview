#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.

Functions:
    makeChange(coins, total): Returns the fewest number of coins needed or -1.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): The values of the coins in your possession.
        total (int): The target amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met.
    """
    # Edge case: If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Edge case: If no coins are provided, return -1
    if not coins:
        return -1

    # Initialize dp array: dp[i] represents the fewest coins to make total i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    # Update dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
