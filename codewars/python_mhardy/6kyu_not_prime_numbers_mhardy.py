# You are given two positive integers a and b (a < b <= 20000). 
# Complete the function which returns a list of all those numbers in the 
# interval [a, b) whose digits are made up of prime numbers (2, 3, 5, 7) 
# but which are not primes themselves.

# Be careful about your timing!

# MY SOLUTION PASSES ALL TESTS, BUT TIMES OUT WITH LARGE RANGES.
# RE-FACTORING/OPTIMIZATION REQUIRED

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def not_primes(a, b):
    res = []
    primes = ['2','3','5','7']
    for i in range(a, b):
        if all([str(y) in primes for y in str(i)]):
            if is_prime(i) == False:
                res.append(i)
    return res

import codewars_test as test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(not_primes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77])
        test.assert_equals(not_primes(2, 77), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75])
        test.assert_equals(not_primes(2700, 3000), [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
        test.assert_equals(not_primes(500, 999), [522, 525, 527, 532, 533, 535, 537, 552, 553, 555, 572, 573, 575, 722, 723, 725, 732, 735, 737, 752, 753, 755, 772, 775, 777])
        test.assert_equals(not_primes(999, 2500), [2222, 2223, 2225, 2227, 2232, 2233, 2235, 2252, 2253, 2255, 2257, 2272, 2275, 2277, 2322, 2323, 2325, 2327, 2332, 2335, 2337, 2352, 2353, 2355, 2372, 2373, 2375])