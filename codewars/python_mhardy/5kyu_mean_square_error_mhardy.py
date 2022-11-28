# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
# Examples
# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2


def solution(array_a, array_b):
    diff_list = []
    sqr_list = []
    for i in range(len(array_a)):
        diff_list.append(int(array_a[i]) - int(array_b[i]))
    for i in diff_list:
        sqr_list.append(i**2)
    return sum(sqr_list) / len(sqr_list)

import codewars_test as test
a1 = [1,2,3]
a2 = [4,5,6]
  
test.assert_approx_equals(solution(a1, a2), 9)

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]

test.assert_approx_equals(solution(b1, b2), 16.5)

c1 = [0, -1]
c2 = [-1, 0]

test.assert_approx_equals(solution(c1, c2), 1)

d1 = [10, 10]
d2 = [10, 10]

test.assert_approx_equals(solution(d1, d2), 0)