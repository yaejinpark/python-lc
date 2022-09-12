# In this Kata, your function receives an array of integers as input. Your task is to determine whether t
# he numbers are in ascending order. An array is said to be in ascending order if there are no two adjacent 
# integers where the left integer exceeds the right integer in value.

# For the purposes of this Kata, you may assume that all inputs are valid, i.e. arrays containing only integers.

# Note that an array of 0 or 1 integer(s) is automatically considered to be sorted in ascending order since all 
# (zero) adjacent pairs of integers satisfy the condition that the left integer does not exceed the right integer in value.



def in_asc_order(arr):
    return arr == sorted(arr)




import codewars_test as test




test.describe("Example Tests")
# Array of 2 integers
arr = [1, 2]
test.assert_equals(in_asc_order(arr), True)

arr = [2, 1]
test.assert_equals(in_asc_order(arr), False)

# Array of 3 integers
arr = [1, 2, 3]
test.assert_equals(in_asc_order(arr), True)

arr = [1, 3, 2]
test.assert_equals(in_asc_order(arr), False)

# More complex cases
arr = [1,4,13,97,508,1047,20058]
test.assert_equals(in_asc_order(arr), True)

arr = [56,98,123,67,742,1024,32,90969]
test.assert_equals(in_asc_order(arr), False)