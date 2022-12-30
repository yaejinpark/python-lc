# The rgb function is incomplete. Complete it so that passing in 
# RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range 
# must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0

    r_hex = hex(r).lstrip('0x')
    if r_hex:
        if len(r_hex) == 1:
            r_hex = '0' + r_hex
    else:
        r_hex = '00'
    
    g_hex = hex(g).lstrip('0x')
    if g_hex:    
        if len(g_hex) == 1:
            g_hex = '0' + g_hex
    else:
        g_hex = '00'
    
    b_hex = hex(b).lstrip('0x')
    if b_hex:
        if len(b_hex) == 1:
            b_hex = '0' + b_hex
    else:
        b_hex = '00'
    return_str =  "{}{}{}".format(r_hex,g_hex,b_hex).upper()

    return return_str


#    JIN'S REFACTORED (MUCH B3TT3R) SOLUTIONS:

# def rgb(r, g, b):
#     rgb_list = ["00" if i <= -1 else "FF" if i > 255 else hex(i)[2:] for i in [r,g,b]]
#     res = ""

#     for i in rgb_list:
#         if len(i) == 1:
#             i = "0" + i
#         for c in i:
#             if c.isalpha():
#                 res += c.upper()
#             else:
#                 res += c
#     return res


# def rgb(r,g,b):
#     return "".join([format(n,"02x").upper() if n > -1 and n <= 255 else "FF" if n > 255 else "00" for n in [r,g,b]])


import codewars_test as test
# from solution import rgb


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")