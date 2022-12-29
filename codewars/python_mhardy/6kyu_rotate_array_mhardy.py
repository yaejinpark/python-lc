# Create a method named "rotate" that returns a given array with the 
# elements inside the array rotated n spaces.

# If n is greater than 0 it should rotate the array to the right. 
# If n is less than 0 it should rotate the array to the left. 
# If n is 0, then it should return the array unchanged.

# Example:

# with array [1, 2, 3, 4, 5]

# n = 1      =>    [5, 1, 2, 3, 4]
# n = 2      =>    [4, 5, 1, 2, 3]
# n = 3      =>    [3, 4, 5, 1, 2]
# n = 4      =>    [2, 3, 4, 5, 1]
# n = 5      =>    [1, 2, 3, 4, 5]
# n = 0      =>    [1, 2, 3, 4, 5]
# n = -1     =>    [2, 3, 4, 5, 1]
# n = -2     =>    [3, 4, 5, 1, 2]
# n = -3     =>    [4, 5, 1, 2, 3]
# n = -4     =>    [5, 1, 2, 3, 4]
# n = -5     =>    [1, 2, 3, 4, 5]
# The rotation shouldn't be limited by the indices available in the array. 
# Meaning that if we exceed the indices of the array it keeps rotating.

# Example:

# with array [1, 2, 3, 4, 5]

# n = 7        =>    [4, 5, 1, 2, 3]
# n = 11       =>    [5, 1, 2, 3, 4]
# n = 12478    =>    [3, 4, 5, 1, 2]

def rotate(data, n):
    if data:
        if n > len(data):
            n = n % len(data)
        elif n < -len(data):
            n = -(-n % len(data))
        if n>0:
            spaces = len(data)-n
            new_list = data[-n:] + data[:spaces]
        elif n<0:
            p = -n
            new_list = data[p:] + data[:p]
        elif n == 0:
            return data
        return new_list
    else:
        return []

# JIN'S BEST PRACTICES SOLUTION:

# def rotate(data, n):
#     if len(data) == 0: return []
#     n = n % len(data)
#     return data[-n:] + data[:-n]


import codewars_test as test
# from solution import rotate

@test.describe("Tests")
def test_group():
    @test.it("Fixed tests")
    def test_case():
        test.assert_equals(rotate([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -3), [4, 5, 1, 2, 3])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 4), [2, 3, 4, 5, 1])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -4), [5, 1, 2, 3, 4])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -5), [1, 2, 3, 4, 5])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 6), [5, 1, 2, 3, 4])
        test.assert_equals(rotate([1, 2, 3, 4, 5], -6), [2, 3, 4, 5, 1])
        test.assert_equals(rotate([True, True, False], 2), [True, False, True])
        test.assert_equals(rotate([1, 2, 3, 4, 5], 12478), [3, 4, 5, 1, 2])
        test.assert_equals(rotate([], 976999), [])
