# https://www.codewars.com/kata/56968ce7753513604b000055/train/python
def pyramid_height(n):
    h = 1
    
    while n > ((h+1)**2):
        h += 1
        n -= (h**2)
    return h