# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
def parse(data):
    # TODO: your code here
    deadfish = 0
    directions = {"i":lambda x:x+1, "d":lambda x: x-1, "s": lambda x:x**2}
    res = []
    
    for c in data:
        if c in directions:
            deadfish = directions[c](deadfish)
        if c == 'o':
            res.append(deadfish)
    return res