# Write a method, that will get an integer array as parameter 
# and will process every number from this array.

# Return a new array with processing every number of the input-array like this:

# If the number has an integer square root, take this, 
# otherwise square the number.

# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# Notes
# The input array will always contain only positive numbers, 
# and will never be empty or null.

import math
def square_or_square_root(arr):
    res = []
    for i in arr:
        if math.sqrt(i).is_integer():
            res.append(math.sqrt(i))
        else:
            res.append(i**2)
    return res

# MUCH BETTER ONE-LINER:

# def square_or_square_root( _a ):
#     return [i**.5 if i**.5 % 1 == 0 else i*i for i in _a]
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            [[4, 3, 9, 7, 2, 1 ], [2, 9, 3, 49, 4, 1]],
            [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
            [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
        ]
        
        for inp, exp in tests:
            test.assert_equals(square_or_square_root(inp), exp)