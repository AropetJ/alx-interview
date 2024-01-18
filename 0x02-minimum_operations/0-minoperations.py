#!/usr/bin/python3
'''0-minoperations.py
'''


def minOperations(n):
    """
    Calculates the minimum number of operations required
    to reach a given number 'n' using only the operations
    of doubling the current number or adding 1 to it.
    Args:
        n (int): The target number.
    Returns:
        int: The minimum number of operations required.
    Examples:
        >>> minOperations(6)
        5
        >>> minOperations(9)
        6
    """
    if n <= 1:
        return 0
    i = 2
    res = 0
    while i <= n:
        if n % i == 0:
            res += i
            n = n / i
        else:
            i += 1
    return int(res)
