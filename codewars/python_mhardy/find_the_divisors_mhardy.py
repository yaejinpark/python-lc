# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
# divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string 
# '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).


def divisors(integer):
    factors = []
    for i in range(2, integer):
        if integer % i == 0:
            factors.append(i)  
    if len(factors) == 0:
        return f"{integer} is prime"
    else:
        return factors


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
