#Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters 
# as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter 
# be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"
# (Use the English alphabet with 26 letters!)


def find_missing_letter(chars):
    numeric_list = [ord(char) for char in chars]
    for i in range(len(numeric_list)-1):
        if numeric_list[i]+1 != numeric_list[i+1]:
            result = chr(numeric_list[i]+1)
    return result

import codewars_test as test

test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')