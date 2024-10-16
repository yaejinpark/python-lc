# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

# Your puzzle answer was 8442.

# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

# Your puzzle answer was 4590.

def calculate_board_score(board, current_nums):
    unmarked_sum = 0
    for row in board:
        for num in row:
            if num not in current_nums:
                unmarked_sum += num
    return unmarked_sum

# Parse input from file
with open('input.txt', 'r') as file:
    row_lists = [line.rstrip() for line in file.readlines()]

# Split the drawn numbers and boards
winning_numbers = row_lists[0].split(',')
winning_numbers = [int(num) for num in winning_numbers]
row_lists = row_lists[2:]  # Skip first two rows (numbers and empty line)

# Initialize boards
boards = []
current_board = []
for row in row_lists:
    if row == '':
        boards.append(current_board)
        current_board = []
    else:
        current_board.append([int(i) for i in row.split()])

# Append the last board (as the loop ends without an empty line)
if current_board:
    boards.append(current_board)

# Part One: Find the first board to win (without exiting)
first_winner_found = False

for i in range(5, len(winning_numbers) + 1):
    current_nums = winning_numbers[:i]
    for board in boards:
        # Check rows
        for row in board:
            if all(num in current_nums for num in row):
                if not first_winner_found:
                    unmarked_sum = calculate_board_score(board, current_nums)
                    final_score = unmarked_sum * current_nums[-1]
                    print(f"BINGO! First Winning Board: {board}")
                    print(f"First Winning Score: {final_score}")
                    first_winner_found = True
                break
        
        # Check columns (transpose to get columns as rows)
        columns = list(zip(*board))
        for col in columns:
            if all(num in current_nums for num in col):
                if not first_winner_found:
                    unmarked_sum = calculate_board_score(board, current_nums)
                    final_score = unmarked_sum * current_nums[-1]
                    print("BINGO! First Winning Board:")
                    for row in board:print(row)
                    print(f"First Winning Score: {final_score}")
                    first_winner_found = True
                break

# Part Two: Find the last board to win

# Track winning boards
winning_boards = set()  # To keep track of boards that have already won
last_winning_board = None
last_winning_score = 0

# Continue drawing numbers until the last board wins
for i in range(5, len(winning_numbers) + 1):
    current_nums = winning_numbers[:i]
    for board_index, board in enumerate(boards):
        if board_index in winning_boards:
            # Skip already winning boards
            continue
        
        # Check rows
        row_wins = any(all(num in current_nums for num in row) for row in board)
        
        # Check columns (transpose to get columns as rows)
        columns = list(zip(*board))
        column_wins = any(all(num in current_nums for num in col) for col in columns)

        if row_wins or column_wins:
            # Mark the board as a winner
            winning_boards.add(board_index)
            unmarked_sum = calculate_board_score(board, current_nums)
            final_score = unmarked_sum * current_nums[-1]
            last_winning_board = board
            last_winning_score = final_score
            
            # If this is the last board to win, calculate and display the final score
            if len(winning_boards) == len(boards):
                print("Last Winning Board:")
                for row in last_winning_board:print(row)
                print(f"Final Score of Last Winning Board: {last_winning_score}")
                break

