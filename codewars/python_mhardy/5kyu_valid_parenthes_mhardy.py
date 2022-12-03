# Write a function that takes a string of parentheses, and determines if the order of 
# the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. 
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    counter = 0
    for i in [*string]:
        if i == "(" and counter >= 0:
            counter += 1
        elif i == ")":
            counter -= 1
        else:
            pass
    if counter == 0:
        return True
    else:
        return False


# JIN'S REGEX SOLUTION

# import re

# def valid_parentheses(string):
#     try:
#         re.compile(string)
#         return True
#     except: return False


import codewars_test as test

@test.describe("Sample Tests")
def tests():
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(valid_parentheses("  ("),False, "should work for '  ('")
        test.assert_equals(valid_parentheses(")test"),False, "should work for ')test'")
        test.assert_equals(valid_parentheses(""),True, "should work for ''")
        test.assert_equals(valid_parentheses("hi())("),False, "should work for 'hi())('")
        test.assert_equals(valid_parentheses("hi(hi)()"),True, "should work for 'hi(hi)()'")