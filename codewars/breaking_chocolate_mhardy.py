# Your task is to split the chocolate bar of given dimension n x m into small squares. 
# Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

# For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break,
# but for size 3 x 1 you must do two breaks.

# If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). 
# Input will always be a non-negative integer.

def break_chocolate(n, m):
    if (n==0) or (m==0):
        return 0
    else:
        return (n*m) - 1


import codewars_test as test


@test.describe("Sample Tests")
def basic_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(break_chocolate(5, 5), 24)
        test.assert_equals(break_chocolate(7, 4), 27)
        test.assert_equals(break_chocolate(1, 1), 0)
        test.assert_equals(break_chocolate(0, 0), 0)
        test.assert_equals(break_chocolate(6, 1), 5)