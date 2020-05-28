import random
import time
from numpy import array #Just for formating
from sudokuSolver import *
import copy
class Board:
    '''
    This class generates a random sudoku solution
    and turns it into a solvable puzzle
    '''
    #Generates a sudoku puzzle
    def __init__(self):
        self.makeSolution()
        #print(array(self.sudoku))
        self.makeGame()
    #Generates a solution to a sudoku board    
    def makeSolution(self):
        self.sudoku = [[0 for i in range(9)] for j in range(9)]
        #All current possible numbers for each row
        rmRows = [{i for i in range(1,10)} for j in range(9)]
        #All current possible numbers for each collumn
        rmCols = [{i for i in range(1,10)} for j in range(9)]
        #All current possible numbers for each grid
        rmGrid = [{i for i in range(1,10)} for j in range(9)]
        for i in range(9):
            for j in range(9):
                #intersection between all possible values at that spot
                poss = rmGrid[(j//3)+((i//3)*3)] & rmCols[j] & rmRows[i]
                # gets a random elemnt from the intersection
                temp = random.sample(poss,1)[0]
                sudokuCp = copy.deepcopy(self.sudoku)
                sudokuCp[i][j] = temp
                #Checks if this new element additions results in a solvable puzzle
                while not solve(copy.deepcopy(sudokuCp)):
                    #removes the wrong element from the intersection
                    poss.remove(temp)
                    #finds a new element
                    temp = random.sample(poss,1)[0]
                    sudokuCp[i][j] = temp
                self.sudoku[i][j] = temp
                rmRows[i].remove(temp)
                rmCols[j].remove(temp)
                rmGrid[(j//3)+((i//3)*3)].remove(temp)
                    
    #Adds a random amount of 0s in the puzzle
    def makeGame(self):
        for i in range(9):
            randList = random.sample([0,1,2,3,4,5,6,7,8],random.randint(4,5))
            for j in randList:
                self.sudoku[i][j] = 0

if (__name__ =="__main__"):
    m = Board()
    print(array(m.sudoku))
    
