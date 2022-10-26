# You are given three integer inputs: length, minimum, and maximum.

# Return a string that:

# Starts at minimum
# Ascends one at a time until reaching the maximum, then
# Descends one at a time until reaching the minimum
# repeat until the string is the appropriate length
# Examples:

#  length: 5, minimum: 1, maximum: 3   ==>  "12321"
#  length: 14, minimum: 0, maximum: 2  ==>  "01210121012101"
#  length: 11, minimum: 5, maximum: 9  ==>  "56789876567"
# Notes:

# length will always be non-negative
# negative numbers can appear for minimum and maximum values
# hyphens/dashes ("-") for negative numbers do count towards the length
# the resulting string must be truncated to the exact length provided
# return an empty string if maximum < minimum or length == 0
# minimum and maximum can equal one another and result in a single number repeated for the length of the string

def ascend_descend(length, minimum, maximum):
    res = ""
    if minimum > maximum:
        return ""
    while len(res) <= length:
        for i in range(minimum, maximum+1):
            res += str(i)
        for i in reversed(range(minimum+1, maximum)):
            res += str(i)
    return res[:length]

import codewars_test as test
# from solution import ascend_descend

@test.describe("Fixed Tests")
def fixed_tests():
    
    @test.it("Example Tests")
    def example_test_cases():
        test.assert_equals(ascend_descend(5, 1, 3), "12321")
        test.assert_equals(ascend_descend(14, 0, 2), "01210121012101")
        test.assert_equals(ascend_descend(11, 5, 9), "56789876567")