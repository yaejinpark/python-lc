# We need the ability to divide an unknown integer into a given 
# number of even parts - or at least as even as they can be. 
# The sum of the parts should be the original value, but each 
# part should be an integer, and they should be as close as possible.

# Complete the function so that it returns an array of integers 
# representing the parts. If the input number is too small to 
# split it into requested amount of parts, the additional parts should 
# have value 0. Ignoring the order of the parts, there is only one 
# valid solution for each input to your function!

# Example:
# split_integer(20, 6)  # returns [3, 3, 3, 3, 4, 4]
# Inputs
# The input to your function will always be valid for this kata.


def split_integer(num, parts):
    print(num, parts)
    res = []
    for part in range(1, parts+1):
        res.append(num//parts)
    if num%parts != 0:
        temp = num%parts
        for i in range(1,temp+1):
            res[-i] += 1
    return res


import codewars_test as test
test.assert_equals(split_integer(10, 1), [10])

test.assert_equals(split_integer(2, 2), [1, 1])

test.assert_equals(split_integer(20, 5), [4, 4, 4, 4, 4])
