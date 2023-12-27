from sudoku_generator import sudoku_generator
from sudoku import clear_cells_for_difficulty


solved_sudoku = sudoku_generator()

# Cleared sudoku for the user to solve
cleared_sudoku = clear_cells_for_difficulty(solved_sudoku.copy(), "easy")

print(solved_sudoku, end="\n\n")
print(cleared_sudoku)
