# Create a function that will take any amount of money and break it down to the smallest number of bills as possible. Only integer amounts will be input, NO floats. This function should output a sequence, where each element in the array represents the amount of a certain bill type. The array will be set up in this manner:

# array[0] ---> represents $1 bills

# array[1] ---> represents $5 bills

# array[2] ---> represents $10 bills

# array[3] ---> represents $20 bills

# array[4] ---> represents $50 bills

# array[5] ---> represents $100 bills

# In the case below, we broke up $365 into 1 $5 bill, 1 $10 bill, 1 $50 bill, and 3 $100 bills.

def give_change(amount):
    change = [0, 0, 0, 0, 0, 0]
    change[5] = (amount // 100)
    x = amount % 100
    change[4] = (x // 50)
    y = x % 50
    change[3] = (y // 20)
    z = y % 20
    change[2] = (z // 10)
    a = z % 10
    change[1] = (a // 5)
    b = a % 5
    change[0] = (b)
    change_array = tuple(change)

    return change_array

import codewars_test as test

@test.describe("Basic Tests")
def test_group():
    @test.it("basic test cases")
    def test_case():
        test.assert_equals(give_change(365), (0,1,1,0,1,3))
        test.assert_equals(give_change(217), (2,1,1,0,0,2))