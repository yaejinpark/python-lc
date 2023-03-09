# To find the volume (centimeters cubed) of a cuboid you use the formula:

# volume = Length * Width * Height

# But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

# It's up to you to find out whether the cuboid has equal sides (= is a cube).

# Return true if the cuboid could have equal sides, return false otherwise.

# Return false for invalid numbers too (e.g volume or side is less than or equal to 0).

# Note: side will be an integer


# Longform brute-force
# def cube_checker(volume, side):
#     flag = False
#     if side ** 3 == volume:
#         flag = True
#     return flag

# Most elegant:
def cube_checker(volume, side):
    return side**3 == volume

import codewars_test as test

test.assert_equals(cube_checker(-12,2), False)
test.assert_equals(cube_checker(8, 3),  False)
test.assert_equals(cube_checker(8, 2),  True)
test.assert_equals(cube_checker(-8,-2), False, "side or volume < 0 are invalid !")
test.assert_equals(cube_checker(0, 0),  False)
test.assert_equals(cube_checker(27, 3), True)
test.assert_equals(cube_checker(1, 5),  False)
test.assert_equals(cube_checker(125, 5),True)
test.assert_equals(cube_checker(125,-5),False)
test.assert_equals(cube_checker(0, 12), False)
test.assert_equals(cube_checker(12, -1),False)
test.assert_equals(cube_checker(1, 1),  True)