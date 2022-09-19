# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    result = 0
    result_list = []
    for i in list(data):
        if i == "i":
            result += 1
        elif i == "s":
            result = result**2
        elif i == "d":
            result -= 1
        elif i == "o":
            result_list.append(result)
        else:
            pass
    return result_list

# Jin's lambda solution
# def parse(data):
#     deadfish = 0
#     directions = {"i":lambda x:x+1, "d":lambda x: x-1, "s": lambda x:x**2}
#     res = []
    
#     for c in data:
#         if c in directions:
#             deadfish = directions[c](deadfish)
#         if c == 'o':
#             res.append(deadfish)
#     return res

import codewars_test as test

@test.describe("Sample tests")
def fixed_tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(parse("ooo"), [0,0,0])
        test.assert_equals(parse("ioioio"), [1,2,3])
        test.assert_equals(parse("idoiido"), [0,1])
        test.assert_equals(parse("isoisoiso"), [1,4,25])
        test.assert_equals(parse("codewars"), [0])
