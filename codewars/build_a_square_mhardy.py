# I will give you an integer. Give me back a shape that is as long and wide as the integer. 
# The integer will be a whole number between 1 and 50.

def generate_shape(n):
    shape_str = ""
    for i in range(n):
        shape_str += "+"*int(n)+"\n"
    return (shape_str)[:-1]


# Jin's optimized code:
# def generate_shape(n):
    # initial = '+'*n + '\n'
    # for i in range(n-1):
        # initial += '+'*n = '\n'
    # return initial[:-1]


import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(generate_shape(3), '+++\n+++\n+++')
    test.assert_equals(generate_shape(8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')