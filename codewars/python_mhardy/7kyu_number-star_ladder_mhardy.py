# Using n as a parameter in the function pattern, where n>0, complete the codes to get the pattern (take the help of examples):

# Note: There is no newline in the end (after the pattern ends)

# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:

# 1
# 1*2
# 1**3
# pattern(10): should return the following:

# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6
# 1******7
# 1*******8
# 1********9
# 1*********10


def pattern(n):
    res = "1"
    if n > 1:
        for i in range(2, n+1):
            res += ("\n1" + ("*"*(i-1)) + "{}".format(i))
    return res

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(pattern(1), "1")
        test.assert_equals(pattern(3),"1\n1*2\n1**3")
        test.assert_equals(pattern(7),"1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")
        test.assert_equals(pattern(20),"1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n1*******8\n1********9\n1*********10\n1**********11\n1***********12\n1************13\n1*************14\n1**************15\n1***************16\n1****************17\n1*****************18\n1******************19\n1*******************20")