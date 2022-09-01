# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

def solution(s):
    n = 2
    if len(s) % 2 == 1:
        s += "_"
    split_list = [s[i:i+n] for i in range(0, len(s), n)]
    return split_list


import codewars_test as test

test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)