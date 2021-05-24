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

def is_valid(puzzle, guess, row, col):
    # if valid, returns True; if not, returns False
    # sudoku rules: only one occurence of each number.
    # let's start with rows, because they're easy:
    row_vals = puzzle[row]
    if guess in row_vals:  # if already present ...
        return False       # ... then it's not valid
    
    # columns are harder, because they're indexes in given rows
    col_vals = [] # create an empty list
    # for i in range:
        # col_vals.append(puzzle[i][col]) # just need to note the row, col as a tuple (?)
    col_vals = [puzzle[i][col] for i in range(9)] # take puzzle, index into i, then index into col, and do that for i in range (9) 
    if guess in col_vals:   # don't completely understand the above--shouldn't it just be "row"?
        # if the guess is in those values, then we return False, because the number has been used.
        return False

    # so far, we've just been figuring out what has been used. Now we need where they are located in the 3*3 grid. (it's 9 * 9 spaces for the whole board)
    row_start = (row // 3)  # remember this: division and then dispose of remainder to tell you which row
                            # the given index is on

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
        # now we check the validity of the guess
        if is_valid(puzzle, guess, row, col):

