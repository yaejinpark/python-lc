def dig_pow(n, p):
    dig=[int(a) for a in str(n)]
    big=0
    for num in dig:
        big += num ** p
        p += 1  
    if (big % n) != 0:  
        return -1
    else:
        return(big/n)

import codewars_test as test

test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)