
def persistence(n):    
    length=len(str(n))
    count =0
    numerals= [*str(n)]
    while length > 1 :
        count += 1
        new=1
        x=0
        while x < length:
            new *= int(numerals[x])
            x+=1
        numerals= [*str(new)]
        length=len(str(new))
    return count

import codewars_test as test


@test.describe("Persistent Bugger.")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)