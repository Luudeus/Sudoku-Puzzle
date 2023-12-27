import numpy as np
from random import shuffle


def is_safe(number, current_position, matrix):
    """Check if number can be placed at current_position without conflicts."""
    # Get row and column from current position
    row, col = current_position

    # Check if number is in the current row or column
    for i in range(9):
        if matrix[row][i] == number or matrix[i][col] == number:
            return False

    # Find the top-left corner of the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    # Check the 3x3 square
    for i in range(3):
        for j in range(3):
            if matrix[start_row + i][start_col + j] == number:
                return False
    return True


def find_empty_location(matrix):
    """Find an empty location in the Sudoku grid."""
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(matrix):
    """Solve the Sudoku puzzle using backtracking."""
    empty_position = find_empty_location(matrix)

    if not empty_position:
        return True  # Sudoku is solved

    row, col = empty_position

    for number in range(1, 10):
        if is_safe(number, (row, col), matrix):
            matrix[row][col] = number
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0

    return False


def sudoku_generator():
    # Initialize a 9x9 matrix filled with zeros
    sudoku_matrix = np.zeros((9, 9), dtype=int)

    # Fill the first row with a shuffled list of numbers from 1 to 9
    first_row_numbers = list(range(1, 10))
    shuffle(first_row_numbers)
    sudoku_matrix[0] = first_row_numbers

    # Check if the sudoku is solved starting from the second row
    if solve_sudoku(sudoku_matrix):
        print("Sudoku grid successfully filled.")
    else:
        print("Failed to fill the Sudoku grid.")

    return sudoku_matrix


if __name__ == "__main__":
    sudoku_generator()
