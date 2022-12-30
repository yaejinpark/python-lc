# Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:

# the first two digits of 1176 form a prime.
# the first two digits of the square 1382976 also form a prime.
# the last two digits of 1176 and 1382976 are the same.
# Given two numbers representing a range (a, b), how many numbers satisfy 
# this property within that range? (a <= n < b)

# Example
# solve(2, 1200) = 1, because only 1176 satisfies this property within the range 2 <= n < 1200. 
# See test cases for more examples. The upper bound for the range will not exceed 1,000,000.

# import gmpy2

# def solve(a,b):

#     matches = 0
#     tests = 0
#     if a < 1176:
#         a = 1
#     for i in range(a,b+1):
#         first_2, last_2 = int(str(i)[:2]), int(str(i)[-2:])
#         if gmpy2.is_prime(first_2):
#             sqr_first, sqr_last = int(str(i**2)[:2]), int(str(i**2)[-2:])
#             if gmpy2.is_prime(sqr_first):
#                 if last_2 == sqr_last:
#                     matches += 1
#                     if tests < 10:
#                         print(i, i**2, first_2, last_2, sqr_first, sqr_last)
#                         tests += 1
#     return matches


ls = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
def solve(a,b):
    i = a
    s = 0
    while i < b:
        if (i*i-i)%100==0 and str(i)[:2] in ls and str(i*i)[:2] in ls:
            s += 1
        i += 1
    return s


import codewars_test as test

test.assert_equals(solve(2, 1200), 1)
test.assert_equals(solve(1176, 1200), 1)
test.assert_equals(solve(2, 100000), 247)
test.assert_equals(solve(2, 1000000), 2549)
test.assert_equals(solve(100000 ,1000000), 2302)