# Given two integers a and b, which can be positive or negative, 
# find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.

def get_sum(a, b):
    num_list = []
    if a == b:
        return a
    elif b < a:
        for i in range(b, a+1):
            num_list.append(i)
        return sum(num_list)
    else:
        for i in range(a, b+1):
            num_list.append(i)
        return sum(num_list)



import codewars_test as test

@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)
        test.assert_equals(get_sum(5,7), 18)
        test.assert_equals(get_sum(2,-5), -12)