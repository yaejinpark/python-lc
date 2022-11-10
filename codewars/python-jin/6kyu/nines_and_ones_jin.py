# https://www.codewars.com/kata/5873b2010565844b9100026d/train/python

def one_two_three(n):
    if n < 1: return [0,0]
    ones = '1'* n if n > 0 else '0'
    nines = '9'*(n//9) + str(n%9) if n%9 else '9'*(n//9)
    return [n,int(ones)] if n < 10 else [int(nines),int(ones)]