# Create a function that returns an array containing 
# the first l numbers from the nth diagonal of Pascal's triangle.

# n = 0 should generate the first diagonal of the triangle (the ones).
# The first number in each diagonal should be 1.
# If l = 0, return an empty array.
# Both n and l will be non-negative integers in all test cases.


def generate_diagonal(n, l):
    # Build the layers of the triangle
    triangle = []
    for i in range(n + l):
        current_row = [0] * (i+1)
        current_row[0], current_row[-1] = 1, 1
        for j in range(1, i):
            left = triangle[i - 1][j - 1]
            right = triangle[i - 1][j]
            current_row[j] = left + right
        triangle.append(current_row)
    # Isolate the starting row of the diagonal, and 
    # iterate through the rows below it
    diagonal = []
    p = 0
    for i in range(n, len(triangle)):
        diagonal.append(triangle[i][p])
        p += 1
    return diagonal


# Best practices from Codewars, time to research math.comb():

# from math import comb

# def generate_diagonal(k, num):
#     return [comb(n, k) for n in range(k, k + num)]


import codewars_test as test
# from solution import generate_diagonal

@test.describe('Sample tests')
def _():
    @test.it('Some tests')
    def _():
        test.assert_equals(generate_diagonal(2, 5),[1, 3, 6, 10, 15])
        test.assert_equals(generate_diagonal(1, 10),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        test.assert_equals(generate_diagonal(3, 7),[1, 4, 10, 20, 35, 56, 84])