class SudokuBoard:

    def __init__(self,board=None) -> None:

        if(board == None):
            #initialize self.board to -1
            self.board = []
            for r in range(9):
                # create a new column
                row = []
                # populate column by -1
                for c in range(9):
                    row.append(-1)
                # append column to board
                self.board.append(row)
        else:
            self.setBoard(board)

    def getBoard(self):
        return self.board

    def setBoard(self,board):
        #check if the board is a 9 by 9 array (col and row)
        if len(board) != 9 or len(board[0]) != 9:
            raise Exception("invalidBoardException")

        #check if board values are valid
        for r in range(9):
            for c in range(9):
                if board[r][c] != -1 and not 1 <= board[r][c] <= 9:
                    raise Exception("invalidValueException")

        self.board = board

    def getRow(self, rowNum):
        self.checkIndex(rowNum)

        return self.board[rowNum-1]

    def setRow(self, rowNum, row):
        #check if rowIndex is valid
        self.checkIndex(rowNum)

        #check if row is length 9
        if len(row) != 9:
            raise Exception("invalidRowException")

        #check if row values are valid
        for val in row:
            if val != -1 and not 1 <= val <= 9:
                raise Exception("invalidValueException")

        # set row, -1 because indecies start from 0
        self.board[rowNum-1] = row

    def getCol(self, colNum):
        self.checkIndex(colNum)

        col = []
        for i in range(9):
            col.append(self.board[i][colNum-1])

        return col

    def setCol(self, colNum, col):
        self.checkIndex(colNum)
        
        if len(col) != 9:
            raise Exception("invalidRowException")

        for c in col:
            if c != -1 and not 1 <= c <= 9:
                raise Exception("invalidValueException")

        for row in range(9):
            self.board[row][colNum-1] = col[row]
    
    def getBox(self,rowNum,colNum):
        self.checkIndex(rowNum)
        self.checkIndex(colNum)

        startRow = ((rowNum-1) // 3) * 3
        startCol = ((colNum-1) // 3) * 3
    
        box = []
        for r in range(startRow, startRow+3):
            for c in range(startCol, startCol+3):
                box.append(self.board[r][c])

        return box

    def setBox(self,rowNum,colNum, box):
        self.checkIndex(rowNum)
        self.checkIndex(colNum)

        #check if box is length 9
        if len(box) != 9:
            raise Exception("invalidRowException")

        #check if box values are valid
        for val in box:
            if val != -1 and not 1 <= val <= 9:
                raise Exception("invalidValueException")

        # set box into self.board
        startRow = ((rowNum-1) // 3) * 3
        startCol = ((colNum-1) // 3) * 3

        i = 0
        for r in range(startRow, startRow+3):
            for c in range(startCol, startCol+3):
                self.board[r][c] = box[i]
                i += 1
        
    def getCoordinate(self, rowNum, colNum):
        self.checkIndex(rowNum)
        self.checkIndex(colNum)

        return self.board[rowNum-1][colNum-1]

    def setCoordinate(self, rowNum, colNum, val):
        self.checkIndex(rowNum)
        self.checkIndex(colNum)

        if val != -1 and not 1 <= val <= 9:
            raise Exception("invalidValueException")

        self.board[rowNum-1][colNum-1] = val

        
    def checkIndex(self, index):
        if not 1 <= index <= 9:
            raise Exception("indexOutOfBoundsException")
