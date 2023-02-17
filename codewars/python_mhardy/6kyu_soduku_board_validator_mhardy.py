# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to 
# fill all cells of the grid with digits from 1 to 9, so that each column, 
# each row, and each of the nine 3x3 sub-grids (also known as blocks) 
# contain all of the digits from 1 to 9.
# More info at: http://en.wikipedia.org/wiki/Sudoku

# Sudoku Solution Validator
# Write a function that accepts a Sudoku board, and returns true if it is a 
# valid Sudoku solution, or false otherwise. The cells of the input Sudoku board 
# may also contain 0's, which will represent empty cells. Boards containing one 
# or more zeroes are considered to be invalid solutions.

# Examples
# Valid board:

#   5 3 4|6 7 8|9 1 2
#   6 7 2|1 9 5|3 4 8
#   1 9 8|3 4 2|5 6 7
#   -----+-----+-----
#   8 5 9|7 6 1|4 2 3
#   4 2 6|8 5 3|7 9 1
#   7 1 3|9 2 4|8 5 6
#   -----+-----+-----
#   9 6 1|5 3 7|2 8 4
#   2 8 7|4 1 9|6 3 5
#   3 4 5|2 8 6|1 7 9
# Invalid board:
                
#               This column has two 3's
#                         v
# This cell has a 0 > 0 3 4|6 7 8|9 1 2
#                     6 7 2|1 9 5|3 4 8
#                     1 9 8|3 4 2|5 6 7
#                     -----+-----+-----
#                     8 5 9|7 6 1|4 2 3
#                     4 2 6|8 5 3|7 9 1
#                     7 1 3|9 2 4|8 5 6
#                     -----+-----+-----
#     This box has   /9 6 1|5 3 7|2 8 4
#          two 3's >| 2 8 3|4 1 9|6 3 5 < This row has two 3's
#                    \3 4 5|2 8 6|1 7 9
# Details
# All inputs are guaranteed to be 2D boards of size 9x9 with possible values in range 0-9.
# Rows, columns and blocks (3x3 small squares) must contain each number from range 1-9 exactly once.
# User solution must not modify input boards.

def validate_sudoku(board):
	for row in range(len(board)):
		# Build lists containing sub-squares, every 3 rows
		if row == 0 or row % 3 ==0:
			list1 = board[row][:3]+board[row+1][:3]+board[row+2][:3]
			list2 = board[row][3:6]+board[row+1][3:6]+board[row+2][3:6]
			list3 = board[row][6:]+board[row+1][6:]+board[row+2][6:]
		# Check sub-squares for duplicate numbers
			if len(set(list1)) != len(list1) or \
				len(set(list2)) != len(list2) or \
					len(set(list3)) != len(list3):
				return False
		# Check rows for zeroes
		if 0 in board[row]:
			return False
		for num in range(len(board[row])):
			for j in range(row+1, len(board)):
				# Check Columns and rows for duplicates and zeroes
				if board[j][num] == board[row][num] or \
					board[row].count(board[row][num]) != 1 or \
						board[j][num] == 0:
					return False
	return True


import codewars_test as test

@test.describe("Tests")
def test_suite(): 
    
    fixed_boards = [
                ([[5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5],
				  [5,5,5,5,5,5,5,5,5]], False), # A board full of fives
                ([[1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9],
				  [1,2,3,4,5,6,7,8,9]], False), # All rows are 1..9
                ([[1,1,1,1,1,1,1,1,1],
				  [2,2,2,2,2,2,2,2,2],
				  [3,3,3,3,3,3,3,3,3],
				  [4,4,4,4,4,4,4,4,4],
				  [5,5,5,5,5,5,5,5,5],
				  [6,6,6,6,6,6,6,6,6],
				  [7,7,7,7,7,7,7,7,7],
				  [8,8,8,8,8,8,8,8,8],
				  [9,9,9,9,9,9,9,9,9]], False),  # All cols are 1..9
                ([[5,3,4,6,7,8,9,1,2],
				  [6,7,2,1,9,5,3,4,8],
				  [1,9,8,3,4,2,5,6,7],
				  [8,5,9,7,6,1,4,2,3],
				  [4,2,6,8,5,3,7,9,1],
				  [7,1,3,9,2,4,8,5,6],
				  [9,6,1,5,3,7,2,8,4],
				  [2,8,7,4,1,9,6,3,5],
				  [3,4,5,2,8,6,1,7,9]], True),
                ([[1,3,2,5,7,9,4,6,8],
				  [4,9,8,2,6,1,3,7,5],
				  [7,5,6,3,8,4,2,1,9],
				  [6,4,3,1,5,8,7,9,2],
				  [5,2,1,7,9,3,8,4,6],
				  [9,8,7,4,2,6,5,3,1],
				  [2,1,4,9,3,5,6,8,7],
				  [3,6,5,8,1,7,9,2,4],
				  [8,7,9,6,4,2,1,5,3]], True),
                ([[7,8,4,1,5,9,3,2,6],
				  [5,3,9,6,7,2,8,4,1],
				  [6,1,2,4,3,8,7,5,9],
				  [9,2,8,7,1,5,4,6,3],
				  [3,5,7,8,4,6,1,9,2],
				  [4,6,1,9,2,3,5,8,7],
				  [8,7,6,3,9,4,2,1,5],
				  [2,4,3,5,6,1,9,7,8],
				  [1,9,5,2,8,7,6,3,4]], True),
                ([[9,2,6,5,8,3,4,7,1],
				  [7,1,3,4,2,6,9,8,5],
				  [8,4,5,9,7,1,3,6,2],
				  [3,6,2,8,5,7,1,4,9],
				  [4,7,1,2,6,9,5,3,8],
				  [5,9,8,3,1,4,7,2,6],
				  [6,5,7,1,3,8,2,9,4],
				  [2,8,4,7,9,5,6,1,3],
				  [1,3,9,6,4,2,8,5,7]], True),
                ([[7,1,5,6,2,3,8,4,9],
				  [6,2,4,8,1,9,3,7,5],
				  [3,9,8,7,4,5,6,2,1],
				  [5,3,9,2,7,6,4,1,8],
				  [4,6,2,1,9,8,5,3,7],
				  [8,7,1,5,3,4,9,6,2],
				  [2,5,3,9,6,7,1,8,4],
				  [1,8,6,4,5,2,7,9,3],
				  [9,4,7,3,8,1,2,5,6]], True),
                ([[7,8,3,4,5,6,1,2,9],
				  [6,9,2,1,8,7,3,4,5],
				  [1,4,5,2,3,9,6,7,8],
				  [8,1,7,3,6,2,9,5,4],
				  [5,6,4,7,9,8,2,1,3],
				  [3,2,9,5,4,1,8,6,7],
				  [4,7,6,8,2,3,5,9,1],
				  [9,3,1,6,7,5,4,8,2],
				  [2,5,8,9,1,4,7,3,6]], True),
                ([[1,7,3,2,6,8,9,5,4],
				  [4,2,5,1,9,3,7,6,8],
				  [8,6,9,7,4,5,1,2,3],
				  [6,1,2,8,3,7,4,9,5],
				  [3,9,8,4,5,6,2,1,7],
				  [5,4,7,9,1,2,3,8,6],
				  [9,5,4,3,8,1,6,7,2],
				  [2,3,6,5,7,9,8,4,1],
				  [7,8,1,6,2,4,5,3,9]], True),
                ([[8,4,7,2,6,5,1,9,3],
				  [1,3,6,7,9,8,2,4,5],
				  [9,5,2,1,4,3,8,6,7],
				  [4,2,9,6,7,1,5,3,8],
				  [6,7,8,5,3,2,9,1,4],
				  [3,1,5,4,8,9,7,2,6],
				  [5,6,4,9,1,7,3,8,2],
				  [7,8,1,3,2,4,6,5,9],
				  [2,9,3,8,5,6,4,7,1]], True),
                ([[8,4,7,2,6,5,1,0,3],
				  [1,3,6,7,0,8,2,4,5],
				  [0,5,2,1,4,3,8,6,7],
				  [4,2,0,6,7,1,5,3,8],
				  [6,7,8,5,3,2,0,1,4],
				  [3,1,5,4,8,0,7,2,6],
				  [5,6,4,0,1,7,3,8,2],
				  [7,8,1,3,2,4,6,5,0],
				  [2,0,3,8,5,6,4,7,1]], False), # a valid board, but with 0 instead of 9
                ([[1,3,2,5,7,9,4,6,8],
				  [4,9,8,2,6,1,3,7,5],
				  [7,5,6,3,8,4,2,1,9],
				  [6,4,3,1,5,8,7,9,2],
				  [5,2,1,7,9,3,8,4,6],
				  [9,8,7,4,2,6,5,3,1],
				  [2,1,4,9,3,5,6,8,7],
				  [3,6,5,8,1,7,9,2,4],
				  [8,7,9,6,4,2,1,3,5]], False), # duplicated '3' in eighth column
                ([[1,2,3,4,5,6,7,8,9],
				  [2,3,4,5,6,7,8,9,1],
				  [3,4,5,6,7,8,9,1,2],
				  [4,5,6,7,8,9,1,2,3],
				  [5,6,7,8,9,1,2,3,4],
				  [6,7,8,9,1,2,3,4,5],
				  [7,8,9,1,2,3,4,5,6],
				  [8,9,1,2,3,4,5,6,7],
				  [9,1,2,3,4,5,6,7,8]], False), # valid rows and cols, but invalid boxes
                ([[0,3,4,6,7,8,9,1,2],
				  [6,7,2,1,9,5,3,4,8],
				  [1,9,8,3,4,2,5,6,7],
				  [8,5,9,7,6,1,4,2,3],
				  [4,2,6,8,5,3,7,9,1],
				  [7,1,3,9,2,4,8,5,6],
				  [9,6,1,5,3,7,2,8,4],
				  [2,8,7,4,1,9,6,3,5],
				  [3,4,5,2,8,6,1,7,9]], False),
                ([[1,2,3,4,5,6,6,9,9],
				  [4,5,6,6,9,9,1,2,3],
				  [6,9,9,1,2,3,4,5,6],
				  [2,3,4,5,6,6,9,9,1],
				  [5,6,6,9,9,1,2,3,4],
				  [9,9,1,2,3,4,5,6,6],
				  [3,4,5,6,6,9,9,1,2],
				  [6,6,9,9,1,2,3,4,5],
				  [9,1,2,3,4,5,6,6,9]], False),
                ([[1,2,3,1,2,3,1,2,3],
				  [4,5,6,4,5,6,4,5,6],
				  [7,8,9,7,8,9,7,8,9],
				  [2,3,1,2,3,1,2,3,1],
				  [5,6,4,5,6,4,5,6,4],
				  [8,9,7,8,9,7,8,9,7],
				  [3,1,2,3,1,2,3,1,2],
				  [6,4,5,6,4,5,6,4,5],
				  [9,7,8,9,7,8,9,7,8]], False),
                ([[1,2,3,4,5,6,7,8,9],
				  [4,5,6,7,8,9,1,2,3],
				  [7,8,9,1,2,3,4,5,6],
				  [1,2,3,4,5,6,7,8,9],
				  [4,5,6,7,8,9,1,2,3],
				  [7,8,9,1,2,3,4,5,6],
				  [1,2,3,4,5,6,7,8,9],
				  [4,5,6,7,8,9,1,2,3],
				  [7,8,9,1,2,3,4,5,6]], False)  # valid boxes and rows, repeats in cols
              ]
    
    def clone(board):
        return [row[:] for row in board]
    def stringify(board):            
        def strrow(row):
            return f"{row[0]}{row[1]}{row[2]}|{row[3]}{row[4]}{row[5]}|{row[6]}{row[7]}{row[8]}"
        rows = [strrow(row) for row in board]
        rows.insert(6, "---+---+---")
        rows.insert(3, "---+---+---")
        return "\n".join(rows)
    
    def do_test(board, expected):
        input = clone(board)
        actual = validate_sudoku(input)
        test.assert_equals(actual, expected, f"Incorrect answer for board:\n\n{stringify(board)}\n")
        test.assert_equals(input, board, "Input board must not be modified")       
    
    
    @test.it("Fixed tests")
    def fixed_tests():        
        for board, expected in fixed_boards:
            do_test(board, expected)