from random import randint
from SudokuBoard import SudokuBoard
from SudokuSolver import SudokuSolver

# generates and returns a sudoku board
def generateBoard():
    board = SudokuBoard()

    # add values 1-9 in random spots (does not matter if the same spot)
    for val in range(1,10):
        while True:
            r = randint(1,9)
            c = randint(1,9)

            # if we already set the coordinate r,c, get another coordinate
            if(board.getCoordinate(r,c) == -1):
                board.setCoordinate(r,c,val)
                break
        

    # solve board and assign to board (dont need the boolean)
    board = SudokuSolver(board)[1]

    # take out 45 numbers from the board
    for i in range(45):
        while True:
            r = randint(1,9)
            c = randint(1,9)

            # if we already reset the coordinate r,c, get another coordinate
            if(board.getCoordinate(r,c) != -1):
                board.setCoordinate(r,c,-1)
                break

    return board
