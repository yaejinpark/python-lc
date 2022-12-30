# We are interested in collecting the sets of six prime numbers, that 
# having a starting prime p, the following values are also primes forming 
# the sextuplet [p, p + 4, p + 6, p + 10, p + 12, p + 16]

# The first sextuplet that we find is [7, 11, 13, 17, 19, 23]

# The second one is [97, 101, 103, 107, 109, 113]

# Given a number sum_limit, you should give the first sextuplet which 
# sum (of its six primes) surpasses the sum_limit value.

# find_primes_sextuplet(70) == [7, 11, 13, 17, 19, 23]

# find_primes_sextuplet(600) == [97, 101, 103, 107, 109, 113]
# Features of the tests:

# Number Of Tests = 18
# 10000 < sum_limit < 29700000

from gmpy2 import is_prime,next_prime

def find_primes_sextuplet(sum_limit):
    i = (sum_limit-30)//6
    while True:
        candidates = [i,i+4,i+6,i+10,i+12,i+16]
        if all(is_prime(j) for j in candidates):
            if sum(candidates) > sum_limit:
                return candidates
        i = next_prime(i)

import codewars_test as test

test.describe("Example Tests")
test.assert_equals(find_primes_sextuplet(70),
[7, 11, 13, 17, 19, 23])

test.assert_equals(find_primes_sextuplet(600),
[97, 101, 103, 107, 109, 113])

test.assert_equals(find_primes_sextuplet(2000000),
[1091257, 1091261, 1091263, 1091267, 1091269, 
1091273])