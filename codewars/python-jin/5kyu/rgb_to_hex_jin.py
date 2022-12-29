# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
def rgb(r, g, b):
    rgb_list = ["00" if i <= -1 else "FF" if i > 255 else hex(i)[2:] for i in [r,g,b]]
    res = ""

    for i in rgb_list:
        if len(i) == 1:
            i = "0" + i
        for c in i:
            if c.isalpha():
                res += c.upper()
            else:
                res += c
    return res

# Thanks Henry... you asshole. 2nd edit.
def rgb(r,g,b):
    return "".join([format(n,"02x").upper() if n > -1 and n <= 255 else "FF" if n > 255 else "00" for n in [r,g,b]])

test1 = rgb(0,0,0)
test2 = rgb(1,2,3)
test3 = rgb(255,255,255)
test4 = rgb(254,253,252)
test5 = rgb(-20,275,125)

print(test1)