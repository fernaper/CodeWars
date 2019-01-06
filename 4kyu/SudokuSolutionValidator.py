"""
	Solution of the problem
	Sudoku Solution Validator
	https://www.codewars.com/kata/529bf0e9bdf7657179000008

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def valid_set(chunk):
    if 0 in chunk:
        return False
    return len(chunk) == len(set(chunk))

def validSolution(board):
    for i in range(9):
        if not valid_set(board[i]):  # Lines
            return False
        if i in [0,3,9]:    # Blocks
            for j in range(3):
                if not valid_set(board[i][j*3:(j+1)*3]+board[i+1][j*3:(j+1)*3]+board[i+2][j*3:(j+1)*3]):
                    return False
        if not valid_set([x[i] for x in board]): # Columns
            return Fals
