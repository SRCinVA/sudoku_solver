def find_next_empty(puzzle):
    # negative spaces are being represented with -1
    # will return based on column and row indices
    # if there are no empyty spaces, you return a tuple (None, None)
    # indices are 0-8
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c  # because you want to fill it
    #"else"
    return None, None # which would mean that you're finished.


def solve_sudoku(puzzle):
    # the "puzzle" is a list of lists that we'll solve using backtracking
    # we'll be mutating the puzzle to be the solution if the solution exists
    # possibly: as you try numbers, you change the list to relfect that you've found a correct one.
    # overall, it sounds like a brute force technique of possible numbers 

    row, col = find_next_empty(puzzle)
    # now perform a validation check
    if row is None: # I believe if could just as easily have been column
        return True # this means that we have solved the puzzle.
    # if we are not finished, then we need to continue to provide guesses (between 1 and 9)
    for guess in range(1,10):
        # now we check the validity
        if is_valid(puzzle, guess, row, col):
