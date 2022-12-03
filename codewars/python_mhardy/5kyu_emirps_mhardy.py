# If you reverse the word "emirp" you will have the word "prime". That idea is related with the 
# purpose of this kata: we should select all the primes that when reversed are a different prime (so palindromic primes should be discarded).

# For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also 
# primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that 
# the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.

# The emirps sequence is registered in OEIS as A006567

# Your task
# Create a function that receives one argument n, as an upper limit, and the return the following array:

# [number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n]

# Examples
# find_emirp(10)
# [0, 0, 0] ''' no emirps below 10 '''

# find_emirp(50)
# [4, 37, 98] ''' there are 4 emirps below 50: 13, 17, 31, 37; largest = 37; sum = 98 '''

# find_emirp(100)
# [8, 97, 418] ''' there are 8 emirps below 100: 13, 17, 31, 37, 71, 73, 79, 97; largest = 97; sum = 418 '''


import gmpy2

def find_emirp(n):
    emirps = []
    for i in range(12, n+1):
        y = int(str(i)[::-1])
        if gmpy2.is_prime(i) == True and gmpy2.is_prime(y) == True and i != y:
            emirps.append(i)
    return [len(emirps) if emirps else 0, max(emirps) if emirps else 0, sum(emirps) if emirps else 0]


import codewars_test as test

test.assert_equals(find_emirp(10), [0, 0, 0])
test.assert_equals(find_emirp(50), [4, 37, 98])
test.assert_equals(find_emirp(100), [8, 97, 418])
test.assert_equals(find_emirp(200), [15, 199, 1489])
test.assert_equals(find_emirp(1000), [36, 991, 16788])