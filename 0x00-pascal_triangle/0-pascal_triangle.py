#!/usr/bin/python3
"""
    A function that returns a list of lists of integers representing
    the Pascal's triangle up to n rows. The outer list represents
    each row and the inner list.
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing
    the Pascal's triangle up to n rows. The outer list represents
    each row and the inner list.

    Args:
        n (int): The integer who's list of Pascal's triangle will be printed
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    triangle = [[1]]
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
