# The Fibonacci numbers are the numbers in the following integer sequence (Fn):

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# such as

# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

# F(n) * F(n+1) = prod.

# Your function productFib takes an integer (prod) and returns an array:

# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.

# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod.

# Some Examples of Return:
# productFib(714) # should return [21, 34, true], 
# productFib(800) # should return [34, 55, false], 


def productFib(prod):
    
    # Build Fib sequence
    fib_list = [0, 1]
    while fib_list[-1] <= prod+5:
        next_value = fib_list[len(fib_list) -1] + fib_list[len(fib_list) - 2]
        fib_list.append(next_value)
    # Find matching pair in list or return first pair that busts limit
    for i in range(len(fib_list)-1):
        if fib_list[i] * fib_list[i+1] == prod:
            return [fib_list[i], fib_list[i+1], True]
        elif fib_list[i] * fib_list[i+1] > prod:
            return [fib_list[i], fib_list[i+1], False]


# BEST PRACTICES FROM CODEWARS:

# def productFib(prod):
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]

import codewars_test as test

test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])