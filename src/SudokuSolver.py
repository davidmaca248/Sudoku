from SudokuBoard import SudokuBoard

# Params: SudokuBoard
# Return: tuple, SudokuBoard and boolean
#         boolean: true if given board is solved
#         SudokuBoard: solved/tried version of the given SudokuBoard
class SudokuSolver:

    def __new__(self,board):
        # check if the board is solvable
        if self.checkSolvable(board):
            self.board = board
            return (self.solveBoard(self),self.board)
        else:
            return (False,board)

    def nextEmpty(self):
        for r in range(1,10):
            for c in range(1,10):
                if(self.board.getCoordinate(r,c) == -1):
                    return (r,c)
        return (None,None)

    # check if the guess is in its row, col, box
    def isValid(self,row,col,guess):
        # row
        rowValues = self.board.getRow(row)
        if guess in rowValues:
            return False

        #col
        colValues = self.board.getCol(col)
        if guess in colValues:
            return False

        #box
        boxValues = self.board.getBox(row,col)
        if guess in boxValues:
            return False

        return True

    def solveBoard(self):

        # get the next empty spot
        row,col = self.nextEmpty(self)

        # check if an empty box is assigned
        if row == None:
            #if no more empty boxes, then board is solved
            return True

        for n in range(1,10):
            if self.isValid(self,row,col,n):
                self.board.setCoordinate(row,col,n)

                if self.solveBoard(self):
                    return True

                self.board.setCoordinate(row,col,-1)
        return False

    # checks if there are duplicates in each row,col,box
    def checkSolvable(board):
        for r in range(1,10):
            row = board.getRow(r)
            # remove -1 from the list
            row = [x for x in row if x != -1]
            # check for duplicates
            if len(row) != len(set(row)):
                return False

        for c in range(1,10):
            col = board.getCol(c)

            col = [x for x in col if x != -1]

            if len(col) != len(set(col)):
                return False

        for r in range(3,10,3):
            for c in range(3,10,3):
                box = board.getBox(r,c)
                
                box = [x for x in box if x != -1]

                if len(box) != len(set(box)):
                    return False

        return True