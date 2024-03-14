#!/usr/bin/python3
"0-prime_game.py"


def isWinner(x, nums):
    """Determines the winner of the prime game.
    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing the numbers
        for each round.
    Returns:
        str: The name of the winner ("Ben" or "Maria").
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, prime in enumerate(primes) if prime]
    primes = primes[1:]
    count = 0
    for i in nums:
        count += sum([1 for prime in primes if prime <= i])
    if count % 2 == 0:
        return "Ben"
    return "Maria"
