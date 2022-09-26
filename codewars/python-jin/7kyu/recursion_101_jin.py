# https://www.codewars.com/kata/5b752a42b11814b09c00005d/train/python
def solve(a,b):
    if a==0 or b==0: # required to break infinite recursion
        return [a,b]
    
    if a >= 2*b: 
        a = a-2*b
    elif b >= 2*a:
        b = b-2*a
    else: return [a,b]
    return solve(a,b)