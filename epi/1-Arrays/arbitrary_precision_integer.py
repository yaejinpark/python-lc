"""
Write a program which takes as input an array of digits encoding a nonnegative decimal integer D 
and updates the array to represent the integer D + 1. 
For example, if the input is (1,2,9) then you should update the array to (1,3,0). 
Your algorithm should work even if it is implemented in a langua ge that has finite-precision arithmetic.
"""

def arb_integer(arr,int_d):
# "Chain" one up in a situation such as <1,9,9> + 1 => <2,0,0>... recursion?
# Alternatively, I can start the for loop from the end of the array.

    # Can't use list.reverse() since it returns None
    i = 0

    while i < len(arr):
        digit_index = (len(arr)-1) - i # in order to start from the smallest digit

        carryover = 0
        if arr[digit_index] + int_d >= 10:
            carryover = 10//(arr[digit_index] + int_d)
            arr[digit_index] = (arr[digit_index] + int_d) % 10
        # Can I add chain carryovers recursively...?
        else:
            arr[digit_index] = arr[digit_index] + int_d

        i += 1
        
    return arr
        
test1_arr = [1,2,9]
test1_int = 1 # sum of test1_arr and test1_int should return [1,3,0]
test2_arr = [1,9,9] # sum of test2_arr and test1_int should return [2,0,0]

print(arb_integer(test1_arr,test1_int))