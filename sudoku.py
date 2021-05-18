def find_next_empty(puzzle):



def solve_sudoku(puzzle):
    # the "puzzle" is a list of lists that we'll solve using backtracking
    # we'll be mutating the puzzle to be the solution if the solution exists
    # possibly: as you try numbers, you change the list to relfect that you've found a correct one.
    # overall, it sounds like a brute force technique of possible numbers 

row, col = find_next_empty():