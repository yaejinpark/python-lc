# Given a rational number n

#  n >= 0, with denominator strictly positive

# as a string (example: "2/3" in Ruby, Python, Clojure, JS, CS, Go)
# or as two strings (example: "2" "3" in Haskell, Java, CSharp, C++, Swift, Dart)
# or as a rational or decimal number (example: 3/4, 0.67 in R)
# or two integers (Fortran)
# decompose this number as a sum of rationals with numerators equal to one and without repetitions
#  (2/3 = 1/2 + 1/6 is correct but not 2/3 = 1/3 + 1/3, 1/3 is repeated).

# The algorithm must be "greedy", so at each stage the new rational obtained in the decomposition
#  must have a denominator as small as possible. In this manner the sum of a few fractions in the 
# decomposition gives a rather good approximation of the rational to decompose.

# 2/3 = 1/3 + 1/3 doesn't fit because of the repetition but also because the first 1/3 has a 
# denominator bigger than the one in 1/2 in the decomposition 2/3 = 1/2 + 1/6.

# Example:
# (You can see other examples in "Sample Tests:")

# decompose("21/23") or "21" "23" or 21/23 should return 

# ["1/2", "1/3", "1/13", "1/359", "1/644046"] in Ruby, Python, Clojure, JS, CS, Haskell, Go

# "[1/2, 1/3, 1/13, 1/359, 1/644046]" in Java, CSharp, C++, Dart

# "1/2,1/3,1/13,1/359,1/644046" in C, Swift, R
# Notes
# The decomposition of 21/23 as

# 21/23 = 1/2 + 1/3 + 1/13 + 1/598 + 1/897
# is exact but don't fulfill our requirement because 598 is bigger than 359. Same for

# 21/23 = 1/2 + 1/3 + 1/23 + 1/46 + 1/69 (23 is bigger than 13)
# or 
# 21/23 = 1/2 + 1/3 + 1/15 + 1/110 + 1/253 (15 is bigger than 13).
# The rational given to decompose could be greater than one or equal to one, in which case the first 
# "fraction" will be an integer (with an implicit denominator of 1).

# If the numerator parses to zero the function "decompose" returns [] (or "",, or "[]").

# The number could also be a decimal which can be expressed as a rational.

from fractions import Fraction
def decompose(n):
    if n == "0":
        return []
    elif "." in list(n):
        factors = [float(n)*100000, 100000]
    else:
        factors = n.split("/")
    
    n1 = int(factors[0])
    n2 = int(factors[1])
    fract_list = []
    string_list = []
    if n1 > n2:
        string_list.append("{}".format(n1 // n2))
        n1 = n1 - n2
        if n1 % n2 != 0:
            if n2 % n1 != 0:
                string_list.append("{}/{}".format(n1 % n2, n2))
            else:
                x = Fraction(n1, n2)
                string_list.append(f"{x.numerator}/{x.denominator}")
            
        return string_list
    
    while n1 != 0:
        x = -(n2 // -n1)
        fract_list.append(x)
        n1 = x * n1 - n2
        n2 = n2 * x

    for i in range(len(fract_list)):
            string_list.append('1/{}'.format(fract_list[i]))

    return string_list


import codewars_test as test

test.assert_equals(decompose('0'), []) 
test.assert_equals(decompose('3/4'), ["1/2", "1/4"]) 
test.assert_equals(decompose('4/5'), ["1/2", "1/4", "1/20"])
test.assert_equals(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])
test.assert_equals(decompose('75/3'), ["25"])
test.assert_equals(decompose('5/4'), ['1', '1/4'])
test.assert_equals(decompose('500/400'), ['1', '1/4'])
test.assert_equals(decompose('8/6'), ['1', '1/3'])