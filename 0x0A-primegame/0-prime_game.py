#!/usr/bin/python3

"""
This script contains the implementation of the prime number game.
Functions:
- isWinner(x, nums): Determines the winner of the game based on optimal moves.
- sieve(n): Generates a list of prime numbers up to a given number using
the Sieve of Eratosthenes.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player that won the most rounds, or None if a tie
    """
    if not nums or x < 1:
        return None

    def sieve(n):
        """
        Generate prime numbers up to n using the Sieve of Eratosthenes.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    primes = sieve(max_num)

    # Precompute the cumulative number of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
