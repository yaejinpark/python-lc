# def mormons(starting_number, reach, target):
#     missions=0
#     while starting_number < target:
#         starting_number += (starting_number*reach)
#         missions += 1    
#     return missions

def mormons(start, reach, target):
    return 0 if start >= target else 1 + mormons(start * (reach + 1), reach, target)

import codewars_test as test

test.describe("Basic tests")
test.assert_equals(mormons(10,3,9),0)#No missions are needed because the number of followers already exceeds target
test.assert_equals(mormons(99,2,99),0)
test.assert_equals(mormons(40,2,120),1)
test.assert_equals(mormons(40,2,121),2)
test.assert_equals(mormons(20000,2,7000000000),12)#Mormons dominate the world!