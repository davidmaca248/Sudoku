from SudokuSolver import SudokuSolver
from SudokuBoard import SudokuBoard
from SudokuUtils import generateBoard
# board 2
board2 = []
for r in range(9):
    # create a new column
    row = []
    # populate column by -1
    for c in range(9):
        row.append(3)
    # append column to board
    board2.append(row)
sudokuBoard2 = SudokuBoard(board2)
solved2,solvedBoard2 = SudokuSolver(sudokuBoard2)

if solved2:
    print("given board 2 is solved")
    for elem in solvedBoard2.getBoard():
        print(elem)
else:
    print("given board 2 is unsolvable")

# board 3
board3 = []
for r in range(9):
    # create a new column
    row = []
    # populate column by -1
    for c in range(9):
        row.append(-1)
    # append column to board
    board3.append(row)

sudokuBoard3 = SudokuBoard(board3)

#change a digit
sudokuBoard3.setCoordinate(1,1,3)
sudokuBoard3.setCoordinate(1,2,9)

solved3,solvedBoard3 = SudokuSolver(sudokuBoard3)

if solved3:
    print("given board 3 is solved")
    for elem in solvedBoard3.getBoard():
        print(elem)
else:
    print("given board 3 is unsolvable")

# board 4
board4 = [
    [3,9,-1, -1,5,-1, -1,-1,-1],
    [-1,-1,-1, 2,-1,-1, -1,-1,5],
    [-1,-1,-1, 7,1,9, -1,8,-1],

    [-1,5,-1, -1, 6, 8, -1,-1,-1],
    [2,-1,6, -1,-1,3, -1,-1,-1],
    [-1,-1,-1, -1,-1,-1, -1,-1,4],
    [5,-1,-1, -1,-1,-1, -1,-1,-1],
    [6,7,-1, 1,-1,5, -1,4,-1],
    [1,-1,9, -1,-1,-1, 2,-1,-1]
]

sudokuBoard4 = SudokuBoard(board4)
solved4,solvedBoard4 = SudokuSolver(sudokuBoard4)

if solved4:
    print("given board 4 is solved")
    for elem in solvedBoard4.getBoard():
        print(elem)
else:
    print("given board 4 is unsolvable")


sudokuBoard5 = generateBoard()
print("board 5: new board")
for elem in sudokuBoard5.getBoard():
    print(elem)