# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"
# Notes
# Other than parentheses only letters and spaces can occur in the string. 
# Don't worry about other brackets like "[]" and "{}" as these will never appear.
# There can be multiple parentheses.
# The parentheses can be nested.


# THANKS TO JIN FOR THIS ONE, I WAS STRIKING OUT WITH A REGEX METHOD

def remove_parentheses(s):
    i,res = 0,''
    
    for c in s:
        if c == '(': i += 1
        if i == 0: res += c
        if c == ')': i -= 1
    return res

import codewars_test as test
@test.describe("remove parentheses")
def tests():
    @test.describe("basic tests")
    def basic():
        test.assert_equals(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        test.assert_equals(remove_parentheses("example (unwanted thing) example"), "example  example")
        test.assert_equals(remove_parentheses("a (bc d)e"), "a e")
        test.assert_equals(remove_parentheses("a(b(c))"), "a")
        test.assert_equals(remove_parentheses("hello example (words(more words) here) something"), "hello example  something")
        test.assert_equals(remove_parentheses("(first group) (second group) (third group)"), "  ")