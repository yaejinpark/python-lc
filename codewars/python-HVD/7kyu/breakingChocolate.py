def break_chocolate(n, m):
    if n == m and n < 2: 
        return 0
    else:
        return ((n*m)-1)

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