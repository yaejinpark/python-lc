# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; 
# he says the gondola lift will take you up to the water source, 
# but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. 
# "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll 
# still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. 
# If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. 
# There are lots of numbers and symbols you don't really understand, but apparently any number 
# adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
# (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
# 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

# def sum_part_numbers(schematic):
#     rows = len(schematic)
#     cols = len(schematic[0])
#     sum_parts = 0

#     def is_symbol(cell):
#         return cell not in '0123456789.'

#     def check_neighbors(r, c):
#         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols and is_symbol(schematic[nr][nc]):
#                 return True
#         return False

#     for r in range(rows):
#         c = 0
#         while c < cols:
#             if schematic[r][c].isdigit():
#                 start = c
#                 while c < cols and schematic[r][c].isdigit():
#                     c += 1
#                 number = int(schematic[r][start:c])
#                 if any(check_neighbors(r, col) for col in range(start, c)):
#                     sum_parts += number
#             else:
#                 c += 1

#     print(sum_parts)

# file = open('input.txt', 'r')
# res_list = [row.rstrip("\n") for row in file.readlines()]
# sum_part_numbers(res_list)

# PART II

# The engineer finds the missing part and installs it in the engine! 
# As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? 
# Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. 
# There stands the engineer, holding a phone in one hand and waving with the other. 
# You're going so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. 
# A gear is any * symbol that is adjacent to exactly two part numbers. 
# Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up 
# so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

def sum_gear_ratios_complete(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    sum_gears = 0

    def is_digit(r, c):
        return 0 <= r < rows and 0 <= c < cols and schematic[r][c].isdigit()

    def extract_number(r, c, dr, dc):
        number = ""
        while is_digit(r, c):
            number += schematic[r][c]
            r += dr
            c += dc
        return int(number) if number else None

    def find_adjacent_parts(r, c):
        if schematic[r][c] != '*':
            return []

        part_numbers = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            if len(part_numbers) < 2 and is_digit(r + dr, c + dc):
                number = extract_number(r + dr, c + dc, dr, dc)
                if number is not None:
                    part_numbers.add(number)

        return list(part_numbers) if len(part_numbers) == 2 else []

    for r in range(rows):
        for c in range(cols):
            if schematic[r][c] == '*':
                adjacent_parts = find_adjacent_parts(r, c)
                if len(adjacent_parts) == 2:
                    sum_gears += adjacent_parts[0] * adjacent_parts[1]

    return sum_gears

schematic_example_complete = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]
print(sum_gear_ratios_complete(schematic_example_complete))


