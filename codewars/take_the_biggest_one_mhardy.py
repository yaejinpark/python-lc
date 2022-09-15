#  https://www.codewars.com/kata/631082840289bf000e95a334/python


# def max_int_chain(n):
#     if n < 5:
#         return -1
#     else:
#         i = n - 2
#         j = 2
#         totals = []
#         while i >= 2:
#             if i == j:
#                 i -= 1
#                 j += 1
#             else:
#                 totals.append(i*j)
#                 i -=1
#                 j +=1
#         return max(totals)

def max_int_chain(n):
    if n < 5:
        return -1
    elif n % 2 == 0:
        return (((n//2)-1)*((n//2)+1))
    else:
        return ((n//2)*(-(n//-2)))


# max_int_chain(6)
# max_int_chain(6)

import codewars_test as test

@test.describe('Fixed Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals(max_int_chain(6), 8, "Incorrect Result")
        test.assert_equals(max_int_chain(10), 24, "Incorrect Result")
        test.assert_equals(max_int_chain(26), 168, "Incorrect Result")
        test.assert_equals(max_int_chain(32), 255, "Incorrect Result")
        test.assert_equals(max_int_chain(36), 323, "Incorrect Result")
        test.assert_equals(max_int_chain(39), 380, "Incorrect Result")
    @test.it("Prime Integers")
    def example_test_case():
        test.assert_equals(max_int_chain(5), 6, "Incorrect Result")
        test.assert_equals(max_int_chain(7), 12, "Incorrect Result")
        test.assert_equals(max_int_chain(11), 30, "Incorrect Result")
        test.assert_equals(max_int_chain(13), 42, "Incorrect Result")
        test.assert_equals(max_int_chain(17), 72, "Incorrect Result")
    @test.it("Starting integer less than 5") 
    def example_test_case():
        test.assert_equals(max_int_chain(1), -1, "Incorrect Result")
        test.assert_equals(max_int_chain(2), -1, "Incorrect Result")
        test.assert_equals(max_int_chain(3), -1, "Incorrect Result")
        test.assert_equals(max_int_chain(4), -1, "Incorrect Result")