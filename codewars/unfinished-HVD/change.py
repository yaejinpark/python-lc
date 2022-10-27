def give_change(amount): 
    change = [0,0,0,0,0,0]
    change[5](amount // 100)
    amount = amount - (100* (amount // 100))
    change[4](amount // 50)
    amount = amount - (50* (amount // 50))
    change[3](amount // 20)
    amount = amount - (20* (amount // 20))
    change[2](amount // 10)
    amount = amount - (10* (amount // 10))
    change[1](amount // 5)
    amount = amount - (5* (amount // 5))
    change[0](amount)
    c_array = tuple(change)

    print (change)
    return c_array


# give_change(365)
import codewars_test as test

@test.describe("Basic Tests")
def test_group():
    @test.it("basic test cases")
    def test_case():
        test.assert_equals(give_change(365), (0,1,1,0,1,3))
        test.assert_equals(give_change(217), (2,1,1,0,0,2))

