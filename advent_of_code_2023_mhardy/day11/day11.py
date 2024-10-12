# --- Day 11: Cosmic Expansion ---
# You continue following signs for "Hot Springs" and eventually come across an observatory. 
# The Elf within turns out to be a researcher studying cosmic expansion using the giant 
# telescope here.

# He doesn't know anything about the missing machine parts; he's only visiting for 
# this research project. However, he confirms that the hot springs are the next-closest 
# area likely to have people; he'll even take you straight there once he's done with 
# today's observation analysis.

# Maybe you can help him with the analysis to speed things up?

# The researcher has collected a bunch of data and compiled the data into a single giant 
# image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# The researcher is trying to figure out the sum of the lengths of the shortest path 
# between every pair of galaxies. However, there's a catch: the universe expanded in the 
# time it took the light from those galaxies to reach the observatory.

# Due to something involving gravitational effects, only some space expands. 
# In fact, the result is that any rows or columns that contain no galaxies should all 
# actually be twice as big.

# In the above example, three columns and two rows contain no galaxies:

#    v  v  v
#  ...#......
#  .......#..
#  #.........
# >..........<
#  ......#...
#  .#........
#  .........#
# >..........<
#  .......#..
#  #...#.....
#    ^  ^  ^
# These rows and columns need to be twice as big; the result of cosmic expansion 
# therefore looks like this:

# ....#........
# .........#...
# #............
# .............
# .............
# ........#....
# .#...........
# ............#
# .............
# .............
# .........#...
# #....#.......
# Equipped with this expanded universe, the shortest path between every pair of 
# galaxies can be found. It can help to assign every galaxy a unique number:

# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# ............6
# .............
# .............
# .........7...
# 8....9.......
# In these 9 galaxies, there are 36 pairs. Only count each pair once; order within 
# the pair doesn't matter. For each pair, find any shortest path between the two 
# galaxies using only steps that move up, down, left, or right exactly one . or # at a time. 
# (The shortest path between two galaxies is allowed to pass through another galaxy.)

# For example, here is one of the shortest paths between galaxies 5 and 9:

# ....1........
# .........2...
# 3............
# .............
# .............
# ........4....
# .5...........
# .##.........6
# ..##.........
# ...##........
# ....##...7...
# 8....9.......
# This path has length 9 because it takes a minimum of nine steps to get from 
# galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). 
#                       Here are some other example shortest path lengths:

# Between galaxy 1 and galaxy 7: 15
# Between galaxy 3 and galaxy 6: 17
# Between galaxy 8 and galaxy 9: 5
# In this example, after expanding the universe, the sum of the shortest path between all 
# 36 pairs of galaxies is 374.

# Expand the universe, then find the length of the shortest path between every pair of 
# galaxies. What is the sum of these lengths?
# ----------------------------------------------------------------------------------------------

# file = open('input.txt', 'r')

# row_lists = []

# for row in file.readlines():
#     row = row.rstrip("\n")
#     row_lists.append(list(row))

# empty_cols = []

# for i in range(len(row_lists[0])):
#     flag = True
#     for l in row_lists:
#         if l[i] == '#':
#             flag = False
#     if flag:
#         empty_cols.append(i)

# gal_dict = {}
# current = 1
# row_num = 1
# file = open('input.txt', 'r')

# for row in file.readlines():
#     row = row.rstrip("\n")
    
#     for i, char in enumerate(list(row)):
#         if char == '#':
#             gal_dict[str(current)] = (row_num, i+1)
#             current += 1
#     if '#' not in row:
#         row_num += 2
#     else:
#         row_num += 1
        
# for i in empty_cols[::-1]:
#     for key, val in gal_dict.items():
#         if val[1] > i:
#             gal_dict[key] = (val[0], val[1]+1)

# dist_dict = {}

# for key, val in gal_dict.items():

#     for other_key, other_val in gal_dict.items():
#         temp = sorted([int(key), int(other_key)])
#         temp = [str(i) for i in temp]
#         label = " ".join(temp)
#         if key == other_key:
#             pass
#         elif label in dist_dict.keys():
#             pass
#         else:
#             x_vals = sorted([val[1], other_val[1]])
#             y_vals = sorted([val[0], other_val[0]])
#             distance = (x_vals[1]-x_vals[0]) + (y_vals[1]-y_vals[0])
#             dist_dict[label] = distance

# print(sum(dist_dict.values()))

# CORRECT ANSWER: 9918828
            
# COORDINATE TESTING SYSTEM

# flag = 'y'
# while flag == 'y':
#     first_gal = input("Which Galaxy is your starting point? (1-440): ")
#     second_gal = input("Which Galaxy is your end point? (1-440): ")
#     if first_gal == second_gal:
#         print("You haven't traveled anywhere, the distance is 0.")
#     else:
#         temp1 = sorted([int(first_gal), int(second_gal)])
#         temp1 = [str(i) for i in temp1]
#         label1 = " ".join(temp1)
#         print(f'The distance between Galaxy {first_gal} {gal_dict[first_gal]} \
#               and Galaxy {second_gal} {gal_dict[second_gal]} is {dist_dict[label1]}')
#         flag = input("Would you like to pick again? (y/n): ")

# ----------------------------------------------------------------------------------------------
# --- Part Two ---
# The galaxies are much older (and thus much farther apart) than the researcher 
# initially estimated.

# Now, instead of the expansion you did before, make each empty row or column one 
# million times larger. That is, each empty row should be replaced with 1000000 
# empty rows, and each empty column should be replaced with 1000000 empty columns.

# (In the example above, if each empty row or column were merely 10 times larger, 
#  the sum of the shortest paths between every pair of galaxies would be 1030. 
#  If each empty row or column were merely 100 times larger, the sum of the shortest 
#  paths between every pair of galaxies would be 8410. However, your universe will 
#  need to expand far beyond these values.)

# Starting with the same initial image, expand the universe according to these new 
# rules, then find the length of the shortest path between every pair of galaxies. 
# What is the sum of these lengths?
# ----------------------------------------------------------------------------------------------

file = open('input.txt', 'r')

# Create lists of row characters to identify empty columns
row_lists = []
for row in file.readlines():
    row = row.rstrip("\n")
    row_lists.append(list(row))

empty_cols = []
# Check if character index is empty in all rows
for i in range(len(row_lists[0])):
    flag = True
    for l in row_lists:
        if l[i] == '#':
            flag = False
    if flag:
        empty_cols.append(i)

file = open('input.txt', 'r')

gal_dict = {}
current = 1
row_num = 1

for row in file.readlines():
    # initialize variable to account for expansion
    empty_space = 0
    row = row.rstrip("\n")
    # Assign coordinates for each node, storing them in dictionary with incremented keys
    for i, char in enumerate(list(row)):
        if char == '#':
            gal_dict[str(current)] = (row_num, i+1+empty_space)
            current += 1
        elif i in empty_cols:
            # add expansion for empty columns, accounting for automatic +1 incrementor
            empty_space += 999999
    # add expansion for empty rows
    if '#' not in row:
        row_num += 1000000
    else:
        row_num += 1

dist_dict = {}

for key, val in gal_dict.items():
    # Calculate distance between each node, store them in new dictionary with
    # dynamically joined key descriptors
    for other_key, other_val in gal_dict.items():
        temp = sorted([int(key), int(other_key)])
        temp = [str(i) for i in temp]
        label = " ".join(temp)
        if key == other_key:
            pass
        elif label in dist_dict.keys():
            pass
        else:
            x_vals = sorted([val[1], other_val[1]])
            y_vals = sorted([val[0], other_val[0]])
            distance = (x_vals[1]-x_vals[0]) + (y_vals[1]-y_vals[0])
            dist_dict[label] = distance

print(sum(dist_dict.values()))

# CORRECT ANSWER: 692506533832

# COORDINATE TESTING SYSTEM
# I built the following testing battery to confirm the distance between 
# two given nodes.

# flag = 'y'
# while flag == 'y':
#     first_gal = input("Which Galaxy is your starting point? (1-440): ")
#     second_gal = input("Which Galaxy is your end point? (1-440): ")
#     if first_gal == second_gal:
#         print("You haven't traveled anywhere, the distance is 0.")
#     else:
#         temp1 = sorted([int(first_gal), int(second_gal)])
#         temp1 = [str(i) for i in temp1]
#         label1 = " ".join(temp1)
#         print(f'The distance between Galaxy {first_gal} {gal_dict[first_gal]} \
#               and Galaxy {second_gal} {gal_dict[second_gal]} is {dist_dict[label1]}')
#         flag = input("Would you like to pick again? (y/n): ")
