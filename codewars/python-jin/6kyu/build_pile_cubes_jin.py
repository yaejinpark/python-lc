# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
from math import sqrt,floor

def find_nb(m):
    # from the equation m = n^2 * (n+1)^2/4
    eq1 = int(0.5*(sqrt(8*sqrt(m)+1)-1))
    return eq1 if (eq1*(eq1+1)//2)**2 == m else -1