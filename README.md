# Sudoku Generator

This project consists of a Sudoku solver, A sudoku board maker and an interface all made in python.

# Solver
## sudokuSolver.py

The solver for this project uses recursive backtracking in order to come up with a solution to a given sudoku board. 
The solve function returns true if the board was able to be solved and false otherwise. 

The checkValid function takes in a board, value, row and column and checks if that value is a valid value for that position.

# Generator
## sudokuBoard.py

This files includes a class named Board that when instantiated, generates a solvable sudoku puzzle.

To determine what are valid values for a given position I created a list of sets of possible values for each row, column and grid in each given position.
I go a position at a time and find the intersection between these sets and place a random number from that intersection into the board if it leads to 
a valid solution.

# Interface
## Grid.py

This file graphically represents a sudoku puzzle using pygame. 

There is a timer and the user has 3 strikes to solve the puzzle. If a user tries to put an invalid number inside of a box it will now be placed. 
This is done by checking if the value that is about to be placed leads to a solution using the solve() from sudokuSolver.py 
