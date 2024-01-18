#!/usr/bin/python3
'''0-minoperations.py
'''


def minOperations(n):
    '''minOperations
    '''
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
