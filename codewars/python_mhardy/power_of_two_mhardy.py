# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) 
# that determines if a given non-negative integer is a power of two. 
# From the corresponding Wikipedia entry:

#a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation 
# with number two as the base and integer n as the exponent.

# You may assume the input is always valid.

# Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.

import codewars_test as test

def power_of_two(x):
    for i in range(0, x+1):
        if (x == 0):
            return False
        elif i ** 2 == x:
            return True
        else:
            pass

# above code still doesn't work


# Jin's awesome Binary solution
# def power_of_two(x):
#   x_bin = bin(x)[2:]
#   return x_bin.count('1') == 1


test.assert_equals(power_of_two(0), False)
test.assert_equals(power_of_two(1), True)
test.assert_equals(power_of_two(2), True)
test.assert_equals(power_of_two(5), False)
test.assert_equals(power_of_two(6), False)
test.assert_equals(power_of_two(4096), True)