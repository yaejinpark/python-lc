def solution(n):
    dict ={ "M" : 1000, "CM" : 900, "D":500, "CD":400, "C": 100, "XC":90, "L": 50, "XL": 40, "X":10, "IX":9, "V":5, "I":1}
    roman = ""
    for k,v in dict.items():
        if  (n//v) >= 4:
            roman += k
            roman += key
            n = n - v*(n//v)
        else:
            roman +=(k*(n//v))
            n = n - v*(n//v)
        key = k
    return (roman)

import codewars_test as test

@test.describe('Testing...')
def _():
    @test.it('Fixed tests')
    def fixed_tests():
        test.assert_equals(solution(1),'I', "solution(1),'I'")
        test.assert_equals(solution(4),'IV', "solution(4),'IV'")
        test.assert_equals(solution(6),'VI', "solution(6),'VI'")
        test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
        test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
        test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
        test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        test.assert_equals(solution(1000), 'M', 'solution(1000), M')
        test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")