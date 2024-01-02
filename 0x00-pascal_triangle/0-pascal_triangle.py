#!/usr/bin/python3
# 0-pascal_triangle

def pascal_triangle(n):
    """ 
    A function that returns a list of lists of integers representing the Pascal's
    triangle up to n rows. The outer list represents each row and the inner list.

    Args:
        n (int): The integer who's list of Pascal's triangle will be printed
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    # If n is 1, return a list with a single list containing 1
    elif n == 1:
        return [[1]]
    
    # Initialize the triangle with the first row
    triangle = [[1]]

    # For each row from the second to the nth
    for i in range(1, n):
        # Initialize the row with a leading 1
        row = [1]
        # For each element from the second to the ith in the row
        for j in range(1, i):
            # Append the sum of the two elements above it in the triangle
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # Append a trailing 1 to the row
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)
    
    # Return the triangle
    return triangle
