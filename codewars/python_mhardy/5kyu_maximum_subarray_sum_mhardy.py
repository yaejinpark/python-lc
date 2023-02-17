# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

# The maximum sum subarray problem consists in finding the maximum 
# sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and 
# the maximum sum is the sum of the whole array. If the list is made
#  up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty 
# list or array is also a valid sublist/subarray.

def max_sequence(arr):
    maximum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if sum(arr[i:j]) > maximum:
                maximum = sum(arr[i:j])
    return maximum

import codewars_test as test

@test.describe("Fixed tests")
def tests():
    
    @test.it("Should work on an empty array")
    def test_empty_array():
        test.assert_equals(max_sequence([]), 0)

    @test.it("Should obtain correct maximum subarray sum in the array from the kata description example")
    def test_example_array():
        test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        
    @test.it("Should obtain correct maximum subarray sum in an example with negative numbers")
    def test_negative_array():
        test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
        
    @test.it("Should obtain correct maximum subarray sum in a complex example")
    def test_complex_array():
        test.assert_equals(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)