# An array is called zero-plentiful if it contains multiple zeros, and every sequence of zeros is at least 4 items long.

# Your task is to return the number of zero sequences if the given array is zero-plentiful, oherwise 0.

# Examples
# [0, 0, 0, 0, 0, 1]  -->  1
# # 1 group of 5 zeros (>= 4), thus the result is 1

# [0, 0, 0, 0, 1, 0, 0, 0, 0]  -->  2
# # 2 group of 4 zeros (>= 4), thus the result is 2

# [0, 0, 0, 0, 1, 0]  -->  0 
# # 1 group of 4 zeros and 1 group of 1 zero (< 4)
# # _every_ sequence of zeros must be at least 4 long, thus the result is 0

# [0, 0, 0, 1, 0, 0]  -->  0
# # 1 group of 3 zeros (< 4) and 1 group of 2 zeros (< 4)

# [1, 2, 3, 4, 5]  -->  0
# # no zeros

# []  -->  0
# # no zeros


def zero_plentiful(arr):
    counter = 0
    total = 0
    for i in arr:
        if i == 0:
            counter += 1
            if counter == 4:
                total += 1
        else:
            if counter < 4 and counter > 0:
                return 0
            counter = 0
    if counter > 3 or counter == 0:
        return total
    else:
        return 0



import codewars_test as test
# from solution import zero_plentiful

@test.describe('Zero-plentiful')
def desc():
    @test.it("Basic tests")
    def it():
        test.assert_equals(zero_plentiful([3]),0)
        test.assert_equals(zero_plentiful([0,0,0,0,0,0]),1)
        test.assert_equals(zero_plentiful([0,0,0,0,0,0,1,2,4,5,0,0,0,0,1]),2)
        test.assert_equals(zero_plentiful([0,0,0,0,0,0,1,0,0]),0)
        test.assert_equals(zero_plentiful([0,0,0,0,0,0,1,0,0,0,0,2,3,4,0,0,0,0,0,0,1,0,0,0,0,0]),4)