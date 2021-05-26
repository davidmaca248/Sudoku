from tkinter import *
import tkinter.font as font
from collections import defaultdict
from SudokuUtils import generateBoard
from SudokuSolver import SudokuSolver
from SudokuBoard import SudokuBoard

class GUI:

    def __init__(self):
        
        self.root = Tk()
        self.root.title("Sudoku")

        # declare board buttons
        self.boardBtns = []
        for r in range(9):
            btnRow = []
            for c in range(9):
                btn = Button(self.root,height=2,width=4,font=font.Font(size=20),command=lambda row=r,col=c:self.boardClick(row,col))        
                btn.grid(row=r+1,column=c)
                btnRow.append(btn)
                
            self.boardBtns.append(btnRow)

        # title label
        self.titleLabel = Label(self.root,text="Sudoku",padx=10,pady=10,font=font.Font(size=20))
        self.titleLabel.grid(row=0,column=3,columnspan=3)

        self.entr = Entry(self.root,width=10)
        self.entr.insert(0,"")
        self.root.bind('<Return>',self.entered)

        # mid panel
        self.msgLabel = Label(self.root,padx=10,pady=12,font=font.Font(size=10))
        self.msgLabel.grid(row=10,column=0,columnspan=3)

        self.cancelBtn = Button(self.root,text="Cancel",height=2,width=10,command=self.cancel)

        # bottom panel
        self.solveBtn = Button(self.root,text="Solve",height=2,width=10,command=self.solve)
        self.solveBtn.grid(row=11,column=0,columnspan=3)

        self.newBoardBtn = Button(self.root,text="New Board",height=2,width=10,command=self.newBoard)
        self.newBoardBtn.grid(row=11,column=3,columnspan=3)

        self.resetBtn = Button(self.root,text="Reset",height=2,width=10,command=self.reset)
        self.resetBtn.grid(row=11,column=6,columnspan=3)

        self.btnColor = self.cancelBtn.cget("background")
        
        #initialize board
        self.initBoard()

        self.root.mainloop()

    def initBoard(self):
        # initial board
        self.board = generateBoard()

        # original Board
        self.origBoard = []
        for elem in self.board.getBoard():
            self.origBoard.append(elem.copy())

        self.origBoard = SudokuBoard(self.origBoard)

        # solved board
        self.solvedBoard = []
        for elem in self.board.getBoard():
            self.solvedBoard.append(elem.copy())

        self.solvedBoard = SudokuBoard(self.solvedBoard)
        self.solvedBoard = SudokuSolver(self.solvedBoard)[1]

        # populate board button text
        for r in range(9):
            for c in range(9):
                txt = self.board.getCoordinate(r+1,c+1)
                btn = self.boardBtns[r][c]
                btn['bg']=self.btnColor
                btn['text'] = txt
                btn['state']="active"
                # disable button if there was already a number on it
                if(txt != -1):
                    btn['state'] = "disabled"
                else:
                    btn['text'] = ""

        # # board buttons
        # self.boardBtns = []
        # for r in range(9):
        #     btnRow = []
        #     for c in range(9):
        #         # get button text
        #         txt = self.board.getCoordinate(r+1,c+1)

        #         btn = Button(self.root,text=str(txt),padx=10,pady=10,command=lambda row=r,col=c:self.boardClick(row,col))        

        #         # disable button if there was already a number on it
        #         if(txt != -1):
        #             btn['state'] = "disabled"
        #         else:
        #             btn['text'] = ""

        #         btn.grid(row=r+1,column=c)
        #         btnRow.append(btn)

        #     self.boardBtns.append(btnRow)
            
        # msg label text
        self.msgLabel['text'] = "Click box to change"

        # list of duplicates in the board
        self.duplicates = defaultdict(list)


    def solve(self):
        # for every button change to solvedBoard
        for r in range(9):
            for c in range(9):
                btn = self.boardBtns[r][c]
                btn['text'] = self.solvedBoard.getCoordinate(r+1,c+1)
                btn['state'] = "disabled"
                btn['bg'] = self.btnColor

        # remove any added components
        self.entr.grid_remove()
        self.cancelBtn.grid_remove()

        # change msgLabel
        self.msgLabel['text'] = "Solved Board"

    def newBoard(self):
        # remove any added components
        self.entr.grid_remove()
        self.cancelBtn.grid_remove()

        self.initBoard()

    def reset(self):
        # for every button change to solvedBoard
        for r in range(9):
            for c in range(9):
                btn = self.boardBtns[r][c]
                btn['bg']=self.btnColor
                txt = self.origBoard.getCoordinate(r+1,c+1)

                if(txt == -1):
                    btn['text'] = ""
                    btn['state'] = "active"
                else:
                    
                    btn['text'] = txt

        # remove any added components
        self.entr.grid_remove()
        self.cancelBtn.grid_remove()

        # reset self.board
        self.board = []
        for elem in self.origBoard.getBoard():
            self.board.append(elem.copy())
 
        # msg label text
        self.msgLabel['text'] = "Click box to change"

        self.board = SudokuBoard(self.board)
        self.duplicates.clear()

    def cancel(self):
        # remove any added components
        self.entr.grid_remove()
        self.cancelBtn.grid_remove()
        self.msgLabel['text'] = "Click box to change"


    def boardClick(self,row,col):
        self.curRow = row
        self.curCol = col

        # mid panel
        self.msgLabel['text'] = f"Enter a value on coordinate ({self.curRow+1},{self.curCol+1}):"
        self.cancelBtn.grid(row=10,column=6,columnspan=3)

        # Entry
        self.entr.delete(0,'end')
        self.entr.grid(row=10,column=3,columnspan=3)

    #input entry
    def entered(self,event):
        val = self.entr.get()

        if(val != ""):

            try:
                val = int(val)
                if(1 <= val <= 9):
                    self.entr.grid_remove()
                    self.cancelBtn.grid_remove()
                    self.msgLabel['text'] = "Click box to change"

                    #change value
                    btn = self.boardBtns[self.curRow][self.curCol]
                    btn['text'] = val
                    

                    self.board.setCoordinate(self.curRow+1,self.curCol+1,val)
                    
                    # check board for duplicates
                    self.checkDuplicates()

                    # check if done
                    if self.checkDone():
                        self.msgLabel['text'] = "YOU WON"
                        # disable board and solve btns
                        for r in range(9):
                            for c in range(9):
                                btn = self.boardBtns[r][c]
                                btn['state'] = "disabled"
                        self.solveBtn['state'] = "disabled"

                else:
                    # if an invalid integer was entered
                    self.msgLabel['text'] = "Enter a digit from 1-9"
            except ValueError:
                # if non-integer was entered
                self.msgLabel['text'] = "Enter an integer!"

    def checkDone(self):
        for r in range(9):
            for c in range(9):
                if self.board.getCoordinate(r+1,c+1) == -1:
                    return False
        return True

    # checks if there are duplicates in the row,col,box of the current button
    def checkDuplicates(self):

        # remove color on rootNode and its duplicates
        if (self.curRow,self.curCol) in self.duplicates:
            #list of duplicates in rootNode
            tup = self.duplicates.pop((self.curRow,self.curCol))

            # for every element in tup check if it appears in duplicates
            for elem in tup:
                if elem in self.duplicates.items():
                    #remove from tup
                    tup.remove(elem)

            # reset color of all buttons in tup
            for r,c in tup:
                self.boardBtns[r][c]['bg'] = self.btnColor

        # check for duplicates
        row = self.board.getRow(self.curRow+1)
        col = self.board.getCol(self.curCol+1)
        box = self.board.getBox(self.curRow+1, self.curCol+1)

        #row
        rowDup = list(self.getDuplicates(row))
        if len(rowDup) != 0:
            #hightlight the duplicates
            for n,i in rowDup:
                for c in i:
                    self.boardBtns[self.curRow][c]['bg'] = "red"
                    self.duplicates[(self.curRow,self.curCol)].append((self.curRow,c))

        # col
        colDup = list(self.getDuplicates(col))
        if len(colDup) != 0:
            for n,i in colDup:
                for r in i:
                    self.boardBtns[r][self.curCol]['bg'] = "red"
                    self.duplicates[(self.curRow,self.curCol)].append((r,self.curCol))

        # box
        boxDup = list(self.getDuplicates(box))
        if len(boxDup) != 0:
            startRow = ((self.curRow) // 3) * 3
            startCol = ((self.curCol) // 3) * 3

            for n,i in boxDup:
                for loc in i:
                    x = 0
                    for r in range(startRow, startRow+3):
                        for c in range(startCol, startCol+3):
                            if x == loc:
                                self.boardBtns[r][c]['bg'] = "red"
                                self.duplicates[(self.curRow,self.curCol)].append((r,c))
                            x += 1

        # remove duplicates from duplicateList
        self.duplicates[(self.curRow,self.curCol)] = list(set(self.duplicates[(self.curRow,self.curCol)]))

    # returns a tuple array of (number, locations list in given array) of duplicates
    @staticmethod
    def getDuplicates(arr):
        # create an empty dictionary
        res = defaultdict(list)
        # for every index,num tuple in arr
        for index,num in enumerate(arr):
            #append index onto the list of key num in res
            res[num].append(index)
        # res now contains all values in arr tupled with a list of their location/s

        # return all tuples in res where list len is > 1 (has duplicates)
        return ((n,iList) 
            for n,iList in res.items() 
                if len(iList)>1 and n != -1)

