#!/usr/bin/python3
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

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
