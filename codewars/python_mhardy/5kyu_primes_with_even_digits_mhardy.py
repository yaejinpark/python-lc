# Find the closest prime number under a certain integer n that has the maximum possible amount of even digits.

# For n = 1000, the highest prime under 1000 is 887, having two even digits (8 twice)

# Naming f(), the function that gives that prime, the above case and others will be like the following below.

# f(1000) ---> 887 (even digits: 8, 8)

# f(1210) ---> 1201 (even digits: 2, 0)

# f(10000) ---> 8887

# f(500) ---> 487

# f(487) ---> 467
# Features of the random tests:

# Number of tests = 28
# 1000 <= n <= 5000000


import gmpy2
            
def f(n):

    max_possible = 0
    result = 0

    for i in range(n-1, 2, -1):
        if gmpy2.is_prime(i) == True:
            possible = 0
            
            for j in str(i):
                if int(j)%2 == 0:
                    possible += 1
            if possible > max_possible:
                max_possible = possible
                result = i

    return result

import codewars_test as test

test.describe("Basic Tests")
test.assert_equals(f(1000), 887)
test.assert_equals(f(1210), 1201)
test.assert_equals(f(10000), 8887)
test.assert_equals(f(500), 487)
test.assert_equals(f(487), 467)
