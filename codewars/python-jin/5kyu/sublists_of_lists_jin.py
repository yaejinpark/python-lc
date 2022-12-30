# https://www.codewars.com/kata/53d3173cf4eb7605c10001a8/train/python

from itertools import combinations as c
def power(a):
    res = []
    for i in range(len(a)+1):
        combos = c(a,i)
        dummy = [list(x) for x in combos]
        res.extend(dummy)
    return res