# Complete the solution so that it returns true if the first 
# argument(string) passed in ends with the 2nd argument (also a string).

def solution(string, ending):
    x = len(ending)
    if ending in string[-x:]:
        return True
    else:
        return False

# Jin's optimized solution
# def solution(string, ending):
    # ending in string[-len(ending):]


import codewars_test as test

test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)