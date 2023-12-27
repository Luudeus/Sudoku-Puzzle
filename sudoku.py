import numpy as np
from random import sample, shuffle

# Function to clear cells in a Sudoku gridbased on difficulty
def clear_cells_for_difficulty(sudoku_matrix, difficulty):
    # Difficulty levels and the number of cells to keep in each 3x3 square
    difficulties = {
        "easy": [2, 3, 4, 4, 4, 5, 5, 6, 6],
        "medium": [2, 2, 3, 3, 3, 3, 4, 5, 5],
        "hard": [2, 2, 2, 3, 3, 3, 4, 4, 4],
        "expert": [0, 1, 2, 3, 3, 3, 3, 5, 5]
    }

    # Shuffle the difficulty list to randomize which numbers are used for each subgrid
    difficulty_list = difficulties.get(difficulty)
    if not difficulty_list:
        raise ValueError(f"Difficulty level '{difficulty}' is not valid. Choose from {list(difficulties.keys())}.")
    shuffle(difficulty_list)  # Shuffle the list to use the numbers in a new order each time

    # Go through each 3x3 subgrid
    for grid_number in range(9):
        # Calculate the starting row and column for the current 3x3 subgrid
        start_row = 3 * (grid_number // 3)
        start_col = 3 * (grid_number % 3)
        subgrid_cells = [(r, c) for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]

        # Determine the number of cells to keep for the current 3x3 subgrid
        cells_to_keep = sample(subgrid_cells, difficulty_list[grid_number])

        # Clear cells that are not in the cells_to_keep list
        for cell in subgrid_cells:
            if cell not in cells_to_keep:
                sudoku_matrix[cell[0]][cell[1]] = 0  # Set cleared cells to 0 or any other placeholder you prefer

    return sudoku_matrix


if __name__ == "__main__":
    clear_cells_for_difficulty(sudoku_matrix, difficulty)
