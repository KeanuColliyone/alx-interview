#!/usr/bin/python3
"""
This module defines the minOperations function.
It calculates the fewest number of operations needed to achieve n H characters.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required.
    using only Copy All and Paste operations.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve n H characters,
        or 0 if n cannot be achieved.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
