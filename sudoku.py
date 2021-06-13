from pprint import pprint

def find_next_empty(puzzle):
    # negative spaces are being represented with -1
    # will return based on column and row indices
    # if there are no empyty spaces, you return a tuple (None, None)
    # indices are 0-8
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c  # because you want to fill it
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
    #col_vals = []  create an empty list
    # for i in range:
        # col_vals.append(puzzle[i][col]) # just need to note the row, col as a tuple (?)
    col_vals = [puzzle[i][col] for i in range(9)] # take puzzle, index into i, then index into col, and do that for i in range (9) 
    if guess in col_vals:   # don't completely understand the above--shouldn't it just be "row"?
        # if the guess is in those values, then we return False, because the number has been used.
        return False

    # so far, we've just been figuring out what has been used. Now we need to know where they are located in the 9 * 9 grid
    # we need to find which index the row of the 3*3 matrix starts at. 
    # ***logic of this: the 3*3 chunks are another dimension of indices and could only be 0, 1, or 2.***
    # do the same for the columns as well
    row_start = (row // 3) * 3  # divide the row index and then dispose of remainder to tell you which row of 3*3 boxes (rows 1, 2, or 3) we're in.
                                # When we multiply that answer by 3, that gives the index (that we originally had, of course)
    # employ the same logic for columns
    col_start = (col // 3) * 3  # we're trying to get these 3 * 3 "chunks"

    # now we have to interate through each set of three throws:
    for r in range(row_start, row_start + 3):   # so that you hit all possible chunks.
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess: # have no recolleciton at all of doing this code ... ?!?!
                return False
    # if we pass all of these checks, then the squares are in fact valid, so we could return True:
    return True


def solve_sudoku(puzzle):
    # the "puzzle" is a list of lists that we'll solve using backtracking
    # we'll be mutating the puzzle to be the solution if the solution exists
    # possibly: as you try numbers, you change the list to relfect that you've found a correct one.
    # overall, it sounds like a brute force technique of possible numbers 

    row, col = find_next_empty(puzzle)
    # now perform a validation check
    if row is None: # Possbily just as easily have been column (and just one has to be None)
        return True # this means that we have solved the puzzle.
    
    #  if we are not finished, then we need to continue to guess (between 1 and 9) until we find one that works.
    for guess in range(1,10):
        # now we check the validity of the guess
        if is_valid(puzzle, guess, row, col): # ... is in fact True, then ...
            # we want to place this guess on the puzzle at that row and column

            puzzle[row][col] = guess
            # What the ... this means that we're "mutating" this puzzle array.
            # now we recursively call this function (presumably to keep mutating things until we get it right.)
            # eventually, we'll solve this puzzle with recursive calls
            # if def solve_sudoku is True, then we return True at the end.
            if solve_sudoku(puzzle):
                return True
            # or, it might not have worked (it might not be valid, or it might need to be backtracked and corrected)
            # in that case:
        puzzle[row][col] = -1  # ... because we didn't place anything there.
            # we're resetting value at that row and column.
            # ultimately, we'll be trying every possible combination for this puzzle.

            # if none of the combinations work, then this puzzle is unsolvable.
    return False

if __name__ == '__main__':
    example_board = [
        [ 3, 9,-1,     -1, 5, -1,   -1, -1, -1],
        [-1,-1,-1,     2, -1, -1,  -1, -1, 5],
        [-1,-1,-1,     2, -1, -1,   -1, 8, -1],

        [-1, 5,-1,    -1, 6, 8,     -1, -1,-1],
        [ 2,-1, 6,    -1, -1, 3,    -1, -1,-1],
        [-1,-1,-1,    -1,-1,-1,     -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,    -1, -1, -1],
        [5, -1, -1,   -1, -1, -1,    -1, -1,-1],
        [1, -1,  9,   -1, -1, -1,    2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)