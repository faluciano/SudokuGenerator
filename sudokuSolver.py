from numpy import array #Just for formating
import sudokuBoard

#Checks if the board is solved
def solved(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True
#Checks if a given move is a valid move
def checkValid(y,x,n,sudoku):
    #checks the collums
    for i in range(9):
        if sudoku[y][i] == n:
            return False
    #checks the row
    for i in range(9):
        if sudoku[i][x]==n:
            return False
    #Gets first value of the square the number is in
    squarex = (x//3)*3
    squarey = (y//3)*3
    #Checks the square
    for i in range(3):
        for j in range(3):
            if sudoku[squarey+i][squarex+j] == n:
                return False
    return True
#Solves the board recursively using backtracking
def solve(sudoku):
    if solved(sudoku):
        #print("done")
        return True
    for y in range(9):
        for x in range(9):
            #Checks if a given spot is empty
            if sudoku[y][x] == 0:
                #Adds a number to the solution with backtracking
                for n in range(1,10):
                    if checkValid(y,x,n,sudoku):
                        sudoku[y][x] = n
                        solve(sudoku)
                        if(not solved(sudoku)):
                            sudoku[y][x] = 0
                return solved(sudoku)

if(__name__ == "__main__"):
    b = sudokuBoard.Board()
    sudoku = b.sudoku
    print("Puzzle: ")
    print(array(sudoku))
    solve(sudoku)
    print("Solution")
    print(array(sudoku))
    