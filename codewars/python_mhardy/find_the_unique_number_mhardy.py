# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i+1] and arr[i] == arr[i-1]:
            return arr[i+1]
        elif arr[i] != arr[i-1] and arr[i] != arr[i-1]:
            if arr[i-1] == arr[i+1]:
                return arr[i]
            else:
                return arr[i-1]
        elif arr[i] != arr[i+1] and (i+1 == len(arr)):
            return arr[i+1]
        else:
            pass

# best practices solution:

# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b


import codewars_test as test

@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
        test.assert_equals(find_uniq([ 10, 3, 3, 3, 3 ]), 10)