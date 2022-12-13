# Your task is to construct a building which will be a pile of n cubes. 
# The cube at the bottom will have a volume of n3 n^3n 
# 3
#  , the cube above will have volume of (n−1)3 (n-1)^3(n−1) 
# 3
#   and so on until the top which will have a volume of 13 1^31 
# 3
#  .

# You are given the total volume m of the building. Being given m can you 
# find the number n of cubes you will have to build?

# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will 
# be an integer m and you have to return the integer n 
# such as n3+(n−1)3+(n−2)3+...+13=m n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = mn 
# 3
#  +(n−1) 
# 3
#  +(n−2) 
# 3
#  +...+1 
# 3
#  =m if such a n exists or -1 if there is no such n.

# Examples:
# findNb(1071225) --> 45

# findNb(91716553919377) --> -1

def find_nb(m):
    res = m
    p = 1
    while res >= 0:
        res -= (p**3)
        p += 1
        if res == 0:
            return p -1
    return -1
    

import codewars_test as test

test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
