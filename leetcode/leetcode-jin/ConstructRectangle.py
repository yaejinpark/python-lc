# https://leetcode.com/problems/construct-the-rectangle/

"""
A web developer needs to know how to design a web page's size.
 So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, 
 whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
"""
def constructRectangle(area):
    options = []
    current_l = 0
    for i in range(1,area+1):
        current_l = i
        if area % i == 0:
            options.append(i)

    middle = len(options)//2
    print(middle)

    return [options[middle],options[middle-1]] if len(options) % 2 == 0 else [options[middle],options[middle]]

# Optimized: don't create a list and find the midpoint right away
def constructRectangle(area):
    middle = int(area ** (1/2))
    while middle > 0:
        if area % middle == 0: 
            return [int(area/middle),middle]
        middle -= 1


print(constructRectangle(4))
print(constructRectangle(122122))
print(constructRectangle(45))