#!/usr/bin/python3
"""UTF-8 Validation
"""
from ast import List


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    Args:
        data (list): list of integers
    Returns:
        True if data is a valid UTF-8 encoding, else return False"""
    count = 0
    n = len(data)
    for i in range(n):
        if count > 0:
            count -= 1
            continue
        if not (0 <= data[i] <= 0x10ffff):
            return False
        elif data[i] <= 0x7f:
            count = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span and all(data[j] & 0b11000000 == 0b10000000
                                     for j in range(i + 1, i + span)):
                count = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span and all(data[j] & 0b11000000 == 0b10000000
                                     for j in range(i + 1, i + span)):
                count = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span and all(data[j] & 0b11000000 == 0b10000000
                                     for j in range(i + 1, i + span)):
                count = span - 1
            else:
                return False
        else:
            return False
    return True
