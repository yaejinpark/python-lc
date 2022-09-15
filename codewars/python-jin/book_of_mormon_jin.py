# https://www.codewars.com/kata/58373ba351e3b615de0001c3/train/python

def mormons(starting_number, reach, target):
    mission_counter = 0
    mormon = starting_number
    
    while mormon < target:
        mormon += mormon * reach
        mission_counter += 1
    
    return mission_counter if target > starting_number else 0

# Using recursion - else is keep adding 1 until the starting_number >= target condition
def mormons(starting_number,reach,target):
    if starting_number >= target:
        return 0
    else:
        return 1 + mormons(starting_number*(reach+1),reach,target)