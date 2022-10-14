# Your task is to calculate the maximum possible height of a perfectly square pyramid 
# (the number of complete layers) that we can build, given n number of cubes as the argument.

# The top layer is always only 1 cube and is always present.
# There are no hollow areas, meaning each layer must be fully populated with cubes.
# The layers are thus so built that the corner cube always covers the inner 25% of the 
# corner cube below it and so each row has one more cube than the one below it.
# If you were given only 5 cubes, the lower layer would have 4 cubes and the top 1 cube 
# would sit right in the middle of them, where the lower 4 cubes meet.

# If you were given 14 cubes, you could build a pyramid of 3 layers, but 13 wouldn't be 
# enough as you would be missing one cube, so only 2 layers would be complete and some cubes left over!

# What is the tallest pyramid possible we can build from the given number of cubes? Simply return the number of complete layers.

# Examples
#  4  -->  1
#  5  -->  2
# 13  -->  2
# 14  -->  3

# props to Henry for solving this one:

def pyramid_height(n):
    height = 1
    while n>((height+1)**2):
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