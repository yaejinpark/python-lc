# Traditionally in FizzBuzz, multiples of 3 are replaced by "Fizz" 
# and multiples of 5 are replaced by "Buzz". But we could also play FizzBuzz 
# with any other integer pair [n, m] whose multiples are replaced with Fizz and Buzz.

# For a sequence of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers whose 
# multiples are being replaced by Fizz and Buzz. Return them as an array [n, m]

# The Fizz and Buzz numbers will always be integers between 1 and 50, and the sequence 
# will have a maximum length of 100. The Fizz and Buzz numbers might be equal, 
# and might be equal to 1.

# Examples
# Classic FizzBuzz; multiples of 3 are replaced by Fizz, multiples of 5 are replaced by Buzz:
# [1, 2, "Fizz", 4, "Buzz", 6]  ==>  [3, 5] 
# Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz:
# [1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]  ==>  [2, 3]
# Multiples of 2 are replaced by Fizz and Buzz:
# [1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]  ==>  [2, 2]
# Fizz = 1, Buzz = 6:
# ["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]  ==>  [1, 6]


def reverse_fizz_buzz(array):
    res = [0,0]
    for i in array:
        num = array.index(i)+1
        if i == "Fizz" and res[0] == 0:
            res[0] += num
        elif i == "Buzz" and res[1] == 0:
            res[1] += num
        elif i == "FizzBuzz":
            if res == [0,0]:
                res = [num,num]
            elif res[0] == 0:
                res[0] += num
            elif res[1] == 0:
                res[1] += num
    return tuple(res)

# CODEWARS MOST CLEVER SOLUTION:

# def reverse_fizz_buzz(array):
#     fizz = array.index("Fizz") if "Fizz" in array else array.index("FizzBuzz")
#     buzz = array.index("Buzz") if "Buzz" in array else array.index("FizzBuzz")
#     return (fizz+1, buzz+1)

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_fizz_buzz([1,2,"Fizz",4,"Buzz"]), (3,5))
        test.assert_equals(reverse_fizz_buzz([1,"Fizz","Buzz","Fizz",5,"FizzBuzz"]), (2,3))
        test.assert_equals(reverse_fizz_buzz([1,"FizzBuzz",3,"FizzBuzz",5,"FizzBuzz"]), (2,2))
        test.assert_equals(reverse_fizz_buzz(["Fizz","Fizz","Fizz","Fizz","Fizz","FizzBuzz"]), (1,6))