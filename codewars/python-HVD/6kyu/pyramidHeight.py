def pyramid_height(n):
    height =1
    while n >((height+1)**2):
        height+=1
        n -= (height**2)      
    return height

import codewars_test as test



def dotest(n, expected):
    test.assert_equals(pyramid_height(n), expected, f"With n = {n}")


@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        for (n, expected) in [(1, 1), (4, 1), (5, 2), (29, 3), (30, 4), (31, 4), (1240, 15), (1241, 15), (1239, 14),
                              (1496, 16), (1495, 15), (4324, 23), (4323, 22), (4899, 23), (4900, 24), (5524, 24),
                              (5525, 25), (6200, 25), (6201, 26), (6254, 26)]:
            dotest(n, expected)
