# Yesterday you found some shoes in your room. 
# Each shoe is described by two values:

# type indicates if it's a left or a right shoe;
# size is the size of the shoe.
# Your task is to check whether it is possible to pair the shoes you found in 
# such a way that each pair consists of a right and a left shoe of an equal size.

# Example
# For:

# shoes = [[0, 21], 
#          [1, 23], 
#          [1, 21], 
#          [0, 23]]
# the output should be true;

# For:

# shoes = [[0, 21], 
#          [1, 23], 
#          [1, 21], 
#          [1, 23]]
# the output should be false.

# Input/Output
# [input] 2D integer array shoes
# Array of shoes. Each shoe is given in the format [type, size], where type is 
# either 0 or 1 for left and right respectively, and size is a positive integer.

# Constraints: 2 ≤ shoes.length ≤ 50,  1 ≤ shoes[i][1] ≤ 100.

# [output] a boolean value

# true if it is possible to pair the shoes, false otherwise.

def pair_of_shoes(shoes):
    shoe_dict = {}
    for i in shoes:
        if i[1] not in shoe_dict.keys():
            if i[0] == 0:
                shoe_dict[i[1]] = 1
            else:
                shoe_dict[i[1]] = 2
        else:
            if i[0] == 0:
                shoe_dict[i[1]] += 1
            else:
                shoe_dict[i[1]] += 2

    for y in shoe_dict.values():
        if y%3 != 0:
            return False
    return True



from copy import deepcopy
# from solution import pair_of_shoes
import codewars_test as test

@test.describe("Tests suite")
def tests():
    def do_test(shoes, expected):
        actual = pair_of_shoes(deepcopy(shoes))
        test.assert_equals(actual, expected, f'for shoes {shoes}:\n')

    @test.it('sample tests')
    def sample_tests():
        do_test([[0, 21], [1, 23], [1, 21], [0, 23]], True)
        do_test([[0, 21], [1, 23], [1, 21], [1, 23]], False)
        do_test([[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]], True)
        do_test([[0, 23], [1, 21], [1, 23], [0, 21]], True)
        do_test([[0, 23], [1, 21], [1, 22], [0, 21]], False)
        do_test([[0, 23]], False)
        do_test([[0, 23], [1, 23]], True)
        do_test([[0, 23], [1, 23], [1, 23], [0, 23]], True)
        do_test([[0, 23], [1, 22]], False)
        do_test([[0, 23], [1, 23], [1, 23], [0, 23], [0, 23], [0, 23]], False)