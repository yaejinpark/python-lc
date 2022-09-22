# Create a function taking a positive integer as its parameter and returning 
# a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately 
# starting with the left most digit and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; 
# or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.

def solution(n):
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    y=12
    result = ""
    while n:
        div = n // nums[y]
        n %= nums[y]

        while div:
            result += roman[y]
            div -= 1
        y -= 1     
    return result




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