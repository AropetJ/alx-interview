#!/usr/bin/python3
'''0-nqueens.py
'''
import sys


def solve_n_queens(N):
    """
    Solve the N-Queens problem and return valid solutions.
    Parameters:
        N (int): The size of the chessboard and the number of
        queens to be placed.
    Returns:
        solutions (list): A list containing valid solutions to
        the N-Queens problem.
    Raises:
        ValueError: If N is less than 4, as the problem is not
        defined for N less than 4.
        TypeError: If N is not an integer.
    """
    if N < 4:
        raise ValueError('N must be at least 4')
    elif not isinstance(N, int):
        raise TypeError('N must be a number')

    solutions = []
    position = []
    for row in range(N):
        for column in range(N):
            first_pos = [row, column]
            if is_valid_position(first_pos, position):
                position.append(first_pos)
                backtrack_n_queens(N, position, 1, solutions)
                position.pop()
    return solutions


def is_valid_position(pos, position):
    """
    Check if a given position is valid for placing a queen on a chessboard.
    Args:
        pos (tuple): The position to check, represented as a
        tuple (row, column).
        position (list): The list of already placed queens' positions.
    Returns:
        bool: True if the position is valid, False otherwise.
    """
    for p in position:
        if p[0] == pos[0] or p[1] == pos[1] or abs(
                p[0] - pos[0]) == abs(p[1] - pos[1]):
            return False
    return True


def backtrack_n_queens(N, position, row, solutions):
    """
    Backtracking algorithm to solve the N-Queens problem.
    Args:
        N (int): The size of the chessboard and the number of queens to be
        placed.
        position (list): A list representing the current state of the board
        with queens' positions.
        row (int): The current row being considered for placing the queen.
        solutions (list): A list to store valid solutions found.
    Returns:
        None: This function does not return a value. It appends valid
        solutions to the 'solutions' list.
    """
    if row == N:
        solutions.append(position.copy())
        return

    for column in range(N):
        pos = [row, column]
        if is_valid_position(pos, position):
            position.append(pos)
            backtrack_n_queens(N, position, row + 1, solutions)
            position.pop()


def print_solutions(solutions):
    """
    Prints tehe solutions for the N-Queens problem.
    Args:
        solutions (list): A list containing solutions to the
        N-Queens problem.
    Returns:
        None: This function does not return a value.
    """
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    try:
        N = int(sys.argv[1])
        solutions = solve_n_queens(N)
        print_solutions(solutions)
    except (ValueError, TypeError) as e:
        print(e)
