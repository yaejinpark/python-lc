from re import X


def divisors(integer):
    factors = []
    while x <= (integer/2):
        print(x)
        x = x+1
    pass



import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(15), [3,5])
        test.assert_equals(divisors(253), [11,23])
        test.assert_equals(divisors(24), [2,3,4,6,8,12])
        test.assert_equals(divisors(25), [5])
        test.assert_equals(divisors(13), "13 is prime")
        test.assert_equals(divisors(3), "3 is prime")
        test.assert_equals(divisors(29), "29 is prime")
