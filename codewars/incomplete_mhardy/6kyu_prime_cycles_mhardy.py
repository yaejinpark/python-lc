# Given an integer n, we can construct a new integer with the following procedure:

# For each digit d in n, find the dth prime number. (If d=0, use 1)
# Take the product of these prime numbers. This is our new integer.
# For example, take 25: The 2nd prime is 3, and the 5th is 11. So 25 would evaluate to 3*11 = 33.

# If we iterate this procedure, we generate a sequence of integers.

# Write a function that, given a positive integer n, returns the maximum value in the sequence starting at n.

# Example: 8 -> 19 -> 46 -> 91 -> 46 -> 91 -> ...
# So the maximum here would be 91.
# 0 <= n <= 10^12

import sympy
prime_list = list(sympy.primerange(0, 1000))
def find_max(n):
    maximum = prime_list[int(list(str(n))[0])]
    max_list = [maximum]
    for x, y in enumerate(list(str(n))[1:]):
        maximum = int(maximum)*prime_list[y-1]
        max_list.append(maximum)

    return max(max_list)


import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    @test.it('Basic tests')
    def example_basic_test_case():
        test.assert_equals(find_max(1), 121)
        test.assert_equals(find_max(2), 121)
        test.assert_equals(find_max(3), 121)
        test.assert_equals(find_max(4), 121)
        test.assert_equals(find_max(5), 121)
        test.assert_equals(find_max(6), 121)
        test.assert_equals(find_max(7), 121)
        test.assert_equals(find_max(8), 91)
        test.assert_equals(find_max(9), 23)
    @test.it('Large tests')
    def example_large_test_case():
        test.assert_equals(find_max(3369196), 4470050)
        test.assert_equals(find_max(2451699), 3177174)
        test.assert_equals(find_max(5364228), 10493301)