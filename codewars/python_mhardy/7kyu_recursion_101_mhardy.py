# In this Kata, you will be given two positive integers a and b and 
# your task will be to apply the following operations:

# i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
# ii) If a ≥ 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
# iii) If b ≥ 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].
# a and b will both be lower than 10E8.

def solve(a,b):
    if a == 0 or b == 0: 
        return [a, b]
    if a>=2*b:
        a = a-(2*b)
    elif b>=(2*a):
        b = b-2*a
    else:
        return [a, b]
    return solve(a, b)

# BEST PRACTICES SOLUTION, INTERESTING STUFF ABOUT USE OF MODULUS:

# '''
# Used the % operator instead of repeated subtraction of a - 2*b or b - 2*a
# Because as long as a > 2*b, the repeated subtraction has to be done and it will 
# eventually give a % 2*b. Repeated subtration in recursion has the problem of
# exceeding the recursion depth, so this approach is better
# '''
# if a == 0 or b == 0:
#     return [a,b]
# elif a >= 2*b:
#     return solve(a % (2*b), b)
# elif b >= 2*a:
#     return solve(a, b % (2*a))
# else:
#     return [a,b]

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(6,19),[6,7])
test.assert_equals(solve(2,1),[0,1])
test.assert_equals(solve(22,5),[0,1])
test.assert_equals(solve(2,10),[2,2])