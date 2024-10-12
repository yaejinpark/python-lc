# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    current=0
    res=[]
    for i in [*data]:
        if i=='i':current+=1
        if i=='d':current-=1
        if i=='s':current**=2
        if i=='o':res.append(current)
    return res

# MOST CLEVER SOLUTION:
# def parse(data):
#     v, r = 0, []
#     for c in data:
#         v, r = v + {'i': 1, 'd': -1, 's': v * (v - 1)}.get(c, 0), r + [v] * (c == 'o')
#     return r


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