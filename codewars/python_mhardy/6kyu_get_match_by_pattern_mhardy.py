# You are given a string with three lowercase letters (pattern).

# Your Task

# Implement a function find_matched_by_pattern(pattern) that returns a predicate function, 
# testing a string input and returning true if the string is matching the pattern or false otherwise.

# A word is considered a match for a given pattern if the first occurence of each letter 
# of the pattern are found in the same order in the word. If a character in the pattern 
# is duplicated, the same logic applies further.

# The pattern will always be a string of size 3.

# Example of use:

# predicate = find_matched_by_pattern('acs')
# predicate('access') # True
# predicate('sacrifice') # False 

def find_matched_by_pattern(pattern):
   
    def match(M, p=pattern):
        for i in M:
            if i == p[0]:
                p = p[1:]
            elif i in p:
                break
            if not p:
                return True

        return False

    return match

import codewars_test as test
@test.describe("Example tests")
def test_group():
    @test.it("Should work for this")
    def test_cases():
        predicate = find_matched_by_pattern('acs')
        test.assert_equals(predicate('access'), True, "'access' is a word that matched pattern 'acs'")
        test.assert_equals(predicate('sacrifice'), False, "'sacrifice' is not a word that matched pattern 'acs'")