#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of a prime game played multiple rounds.

    Args:
        x: The number of rounds.
        nums: A list of n values for each round.

    Returns:
        The name of the player with the most wins ("Maria" or "Ben").
        Returns None if the winner cannot be determined.
    """

    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
            num: The number to check.

        Returns:
            True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)

        moves = 0
        while primes:
            moves += 1
            prime = primes.pop(0)
            multiples = []
            for p in primes:
                if p % prime == 0:
                    multiples.append(p)
            for m in multiples:
                primes.remove(m)

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
