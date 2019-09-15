# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:51:02 2019

@author: Will Pisani

This program will allow a user to play Minesweeper. A lot of the logic and code was reused from https://repl.it/talk/learn/How-to-program-MineSweeper-in-Python-fully-explained-in-depth-tutorial/9397. Hint functionality was my own code.

Program usage:
python minesweeper.py

Libraries needed:
random, string, itertools, copy, sys
"""

# Import necessary libraries

def init_grid(N):
    """
    This function will initialize the minesweeper grid. It will generate the solution grid and the known grid based on a user defined N. It accepts a scalar integer and returns the solution grid and the known grid. Both grids are square.
    """
    
    
    # Initialize solution grid
    sol_grid = [[0 for x in range(N)] for y in range(N)]
    
    # Initialize known grid
    known_grid = [[' ' for x in range(N)] for y in range(N)]
    
    # Generate mines
    for mine in range(0,N):
        placeMine(sol_grid)
        
    # Generate solution
    # Begin looping through cells
    for row in range(0,len(sol_grid)):
        for col in range(0,len(sol_grid[0])):
            value = sol_grid[row][col]
            if value == '*':
                updateSolution(row,col,sol_grid)
    
    return sol_grid, known_grid
    
    
    
def placeMine(sol_grid):
    """
    This function will accept a solution grid and add a mine to it in a random location.
    """
    # Import random library
    import random    
        
    # Get a random location
    row = random.randint(0,len(sol_grid)-1)
    col = random.randint(0,len(sol_grid[0])-1)

    # Check if a mine already exists in that location
    if sol_grid[row][col] != '*':
        sol_grid[row][col] = '*'
    else:
        placeMine(sol_grid)    


def updateSolution(row,col,sol_grid):
    """
    This function wil update the cells around the mines with the appropriate numbering. It will accept the solution grid and the cell where the mine is as input.
    """
    
    # For rows above cell
    if row - 1 > -1: # Checks if row is the first row
        r = sol_grid[row-1]
        
        if col - 1 > -1: # Checks if col is the first column
            # For cells to the top left
            if not r[col - 1] == '*':
                r[col - 1] += 1
        
        # For cells above the mine
        if not r[col] == '*':
            r[col] += 1
        
        # For cells to the top-right of mine
        if len(sol_grid[0]) > col + 1: # Checks if col is the last column
            if not r[col + 1] == '*':
                r[col + 1] += 1
        
    # For cells in the same row as the mine
    r = sol_grid[row]
    
    # For cells to the left of the mine
    if col - 1 > -1: # Checks if col is the first column
        if not r[col - 1] == '*':
            r[col - 1] += 1
    
    # For cells to the right of the mine
    if len(sol_grid[0]) > col + 1: # Checks if col is the last column
        if not r[col + 1] == '*':
            r[col + 1 ] += 1
            
    # For cells in the row below the mine
    if len(sol_grid) > row + 1: # Checks if row is the last row
        r = sol_grid[row + 1]
        
        # For cells to the bottom-left of the mine
        if col - 1 > -1: # Checks if col is the first column
            if not r[col - 1] == '*':
                r[col - 1] += 1
        
        # For cells below the mine
        if not r[col] == '*':
            r[col] += 1
            
        # For cells to the bottom-right of the mine
        if len(sol_grid[0]) > col + 1: # Checks if col is the last column
            if not r[col + 1] == '*':
                r[col + 1] += 1
            
    
def printGrid(grid):
    """
    This function will print out the solution or known grid in a pretty way. It will accept a grid as input.
    """      
#    # Import necessary libraries here    
#    import os
#    os.system('cls')
#    os.system('clear')
    
    # Get size of grid
    N = len(grid)
    
    # Get letters into a string for printing
    # Get the grid header ready for printing
    # Get the grid footer ready for printing
    letter_header = '     '
    first_box_header = '   ╔'
    last_box_header = '   ╚'
    i = 0
    for l in iter_alphabet():
        i += 1
        if i > N:
            break
        else:
            letter_header += l + '   '
            if i == N:
                first_box_header += '═══╗'
                last_box_header += '═══╝'
            else:
                first_box_header += '═══╦'
                last_box_header += '═══╩'
       
    print(letter_header)
    print(first_box_header)
    # Print cells between header and footer
    for row in range(0, N):
        if row > 9:
            column_string = str(row) + ''
        else:
            column_string = str(row) + ' '
        column_box = '   ╠'
        for col in range(0, N):
            if col == N -1:
                column_string += ' ║ ' + str(grid[row][col]) + ' ║'
                column_box += '═══╣'
            else:
                column_string += ' ║ ' + str(grid[row][col])
                column_box += '═══╬'
        print(column_string)  
        if not row == N -1:
            print(column_box)
    
    
    print(last_box_header)
    
    

def iter_alphabet():
    """
    This function will generate a repeating uppercase alphabet.
    Courtesy of Kevin at https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e
    """
    from string import ascii_uppercase
    import itertools
    
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase,repeat=size):
            yield "".join(s)

def getLettersAndNumbers(known_grid):
    """
    This function accepts the known grid and returns two 1D arrays: one with 
    the letters of the columns and one with the numbers of the rows.
    """
    # Get size of known grid
    N = len(known_grid)
    
    # Get array of letters of same length as grid size
    i = 0
    letters = []
    for l in iter_alphabet():
        i += 1
        if i > N:
            break
        else:
            letters.append(l)
    
    # Get array of numbers of same length as grid size
    numbers = [num for num in range(0,N)]
    
    return letters, numbers

def marker(row,col,known_grid):
    """
    This function will place a marker in the given location. It will accept the row and column and the known grid.
    """
    if known_grid[row][col] != ' ':
        print("\nLooks like you meant for the marker to be in a different location.")
        print("Markers may only be placed in blank cells. Please try again.")
        printGrid(known_grid)
    else:
        known_grid[row][col] = 'F'
        printGrid(known_grid)

def getHint(known_grid,sol_grid):
    """
    This function will accept the known grid as input and use it compute the most likely location of a mine (if a player has moved beyond the first turn). 
    It will return the row and column of the most likely mine. If the player is on the first turn, it will suggest a safe cell to open.
    """
    
    # Get length of known grid
    N = len(known_grid)
    
    # Get column letters and row numbers of the known grid
    letters, numbers = getLettersAndNumbers(known_grid)
    

    # Look for a cell that doesn't have a mine and hasn't already been uncovered
    for x in range(N):
        for y in range(N):
            if not sol_grid[x][y] == '*' and not sol_grid[x][y] == known_grid[x][y]:
                print("Try cell {}{}".format(letters[y],numbers[x]))
                return
                    
    
def choose(sol_grid,known_grid):
    """
    This function will ask the player to make a choice as to which cell they want to open. It will accept the solution and known grids as input and return the row and column of the cell.
    """
    
    # Get column letters and row numbers of the known grid
    letters, numbers = getLettersAndNumbers(known_grid)
    
    # Loop in case of invalid entry
    while True:
        
        # Ask for cell to open
        chosen_cell = str(input('Choose a square (eg. A0) or place a marker (eg. mA0).\nIf you would like a hint, type "hint" without quotes: ')).upper()
        print(chosen_cell)
        
        # Check for a valid square
        if chosen_cell.lower() == 'hint':
            getHint(known_grid,sol_grid)
            playGame(sol_grid,known_grid)
            
            
        elif len(chosen_cell) == 3 and chosen_cell[0] == 'M' and chosen_cell[1] in letters and int(chosen_cell[2:]) in numbers:
            row, col = int(chosen_cell[2:]),letters.index(str(chosen_cell[1]))
            marker(row,col,known_grid)
            playGame(sol_grid,known_grid)
            break
        
        elif len(chosen_cell) == 2 and chosen_cell[0] in letters and int(chosen_cell[1:]) in numbers:
            row, col = int(chosen_cell[1:]),letters.index(chosen_cell[0])
            return row,col
        
        else:
            print("Error: invalid input. Please try again.")
            choose(sol_grid,known_grid)
    
    
def zeroProcedure(row,col,known_grid,sol_grid):
    """
    This function is used to do the actual opening of the cells.
    """
    
    # Row above
    if row - 1 > -1: # Checks if the row is the first row
        r = known_grid[row - 1]
        
        if col - 1 > -1: # Checks if col is the first column
            r[col - 1] = sol_grid[row - 1][col - 1]
        
        r[col] = sol_grid[row - 1][col]
        
        if len(sol_grid) > col + 1: # Checks if col is the last column
            r[col + 1] = sol_grid[row - 1][col + 1]
            
    # Same row
    r = known_grid[row]
    
    if col - 1 > -1: # Checks if col is the first column
        r[col - 1] = sol_grid[row][col - 1]
        
    if len(sol_grid) > col + 1: # Checks if col is the last column
        r[col + 1] = sol_grid[row][col + 1]
        
    
    # Row below
    if len(sol_grid) > row + 1: # Checks if row is the last row
        r = known_grid[row + 1]
        if col - 1 > -1: # Checks if col is the first column
            r[col - 1] = sol_grid[row + 1][col - 1]
        
        r[col] = sol_grid[row + 1][col]
        
        if len(sol_grid) > col + 1: # Checks if col is the last column
            r[col + 1] = sol_grid[row + 1][col + 1]
        
            
def checkZeros(known_grid,sol_grid,row,col):
    """
    This function will check if there are other zeros around the cell that has a zero in it. It will open the nearby zero-valued cells.
    """
    # Import necessary libraries
    import copy
    
    # Copy known grid
    oldGrid = copy.deepcopy(known_grid)
    
    # Open the zero-valued cells around the first zero-valued cell
    zeroProcedure(row,col,known_grid,sol_grid)
    
    # Has anything changed
    if oldGrid == known_grid:
        return
    
    # Loop through all of the cells to open up nearby zero-valued cells
    while True:
        oldGrid = copy.deepcopy(known_grid)
        for x in range(len(known_grid)):
            for y in range(len(known_grid[0])):
                if known_grid[x][y] == 0:
                    zeroProcedure(x,y,known_grid,sol_grid)
        
        # If all cells have been opened, return to the game
        if oldGrid == known_grid:
            return
    
    
def playGame(sol_grid,known_grid):
    """
    This function will play the game. It accepts the solution grid and the known grid as input.
    """
    # Import necessary libraries
    import sys
    
    # Have the player choose a cell to open
    row, col = choose(sol_grid,known_grid)
    
    # Get the value of the cell
    value = sol_grid[row][col]
    
    # If they hit a bomb
    if value == '*':
        printGrid(sol_grid)
        print('Sorry! You hit a bomb. You lose the game!')
        
        # Offer to play again
        playAgain = str(input('Play again? (Y/N): ')).upper()
        if playAgain == 'Y':
            N = int(input("How large would you like the grid size?\n"))
            # Initialize the new board
            sol_grid,known_grid = init_grid(N)
            
            # Print the new board
            printGrid(known_grid)
            
            # Play the game
            playGame(sol_grid,known_grid)
        else:
            sys.exit()
    
    # If it didn't hit a bomb, then put the found value into the known grid
    known_grid[row][col] = value
    print(value)
    # Check if that value is a 0
    if value == 0:
        checkZeros(known_grid,sol_grid,row,col)
    
    # Print board
    printGrid(known_grid)
    
    # Checks to see if the player has won the game.
    squaresLeft = 0
    for x in range(0,len(sol_grid)):
        r = known_grid[x]
        squaresLeft += r.count(' ')
        squaresLeft += r.count('F')
    
    if squaresLeft == len(sol_grid):
        printGrid(sol_grid)
        print('Congratulations! You won the game!')
        
        # Offer to play again
        playAgain = str(input('Play again? (Y/N): ')).upper()
        if playAgain == 'Y':
            
            try:
                N = int(input("How large would you like the grid size?\n"))
            except ValueError:
                print("Error: Input must be an integer")
                
            # Initialize the new board
            sol_grid,known_grid = init_grid(N)
        
            # Print the new board
            printGrid(known_grid)
        
            # Play the game
            playGame(sol_grid,known_grid)
        else:
            sys.exit()
            
    # Play another turn
    playGame(sol_grid,known_grid)

def main():
    """
    This function will ask the player the grid size and start the game.
    """
    # Loop in case of invalid entry
    while True:
        try:
            N = int(input("How large would you like the grid size? (e.g. 5)\n"))
            break
        except ValueError:
            print("ERROR: Input must be an integer")
            
    sol_grid, known_grid = init_grid(N)
    
    printGrid(known_grid)
    
    playGame(sol_grid,known_grid)
    
# Start main script
if __name__ == '__main__':
    print("Hi! Welcome to Will Pisani's Python game of Minesweeper!") 
    
    # Call main()
    main()
    