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

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many coins of the current denomination as possible
        count += total // coin
        total %= coin

    return count if total == 0 else -1
