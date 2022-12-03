# The number 81 has a special property, a certain power of the sum of its digits 
# is equal to 81 (nine squared). Eighty one (81), is the first number in having 
# this property (not considering numbers of one digit). The next one, is 512. 
# Let's see both cases with the details

# 8 + 1 = 9 and 92 = 81

# 512 = 5 + 1 + 2 = 8 and 83 = 512

# We need to make a function that receives a number as argument n 
# and returns the n-th term of this sequence of numbers.

# Examples (input --> output)
# 1 --> 81

# 2 --> 512


def power_sumDigTerm(n):
    num_list = []
    
    for i in range(3, 100):
        for z in range(2, 100):
            power = i**z
            digits = [int(i) for i in list(str(power))]
            if sum(digits) == i:
                num_list.append(power)
                   
    return sorted(num_list)[n-1]


import codewars_test as test
# from solution import power_sumDigTerm

def dotest(n, expected):
    actual = power_sumDigTerm(n)
    test.assert_equals(actual, expected, f"With n = {n}")


@test.describe("Tests")
def test_group():
    @test.it("Example tests")
    def test_case():
        for n, expected in [(1, 81), (2, 512), (3, 2401), (4, 4913), (5, 5832)]:
            dotest(n, expected)
            