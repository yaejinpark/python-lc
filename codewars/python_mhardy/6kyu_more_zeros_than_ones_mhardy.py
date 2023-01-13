# Create a moreZeros function which will receive a string for input, 
# and return an array (or null terminated string in C) containing only 
# the characters from that string whose binary representation of its 
# ASCII value consists of more zeros than ones.

# You should remove any duplicate characters, keeping the first occurrence 
# of any such duplicates, so they are in the same order in the final array 
# as they first appeared in the input string.

# Examples

# 'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
#                True       True       False      True       False
                   
#         --> ['a','b','d']
    
# 'DIGEST'--> ['D','I','E','T']
# All input will be valid strings of length > 0. Leading zeros in binary should not be counted.


def more_zeros(s):
    bin_dict = {}
    rtn_list = []
    for i in s:
        bin_dict[i] = bin(ord(i)).lstrip('0b')
    for key, value in bin_dict.items():
        zeroes = 0
        ones = 0
        for i in list(str(value)):
            if i == '0':
                zeroes +=1
            else:
                ones += 1
        if zeroes > ones:
            rtn_list.append(key)   
    return rtn_list


import codewars_test as test

@test.it("Basic tests")
def basic():    
    test.assert_equals(more_zeros('abcde'), ['a', 'b', 'd'])
    test.assert_equals(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
    test.assert_equals(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
    test.assert_equals(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'), ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0'])
    test.assert_equals(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])