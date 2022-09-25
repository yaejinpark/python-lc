# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(string):
    if not string: return {}
    res = {c:0 for c in string}
    for c in string:
        if c in res:
            res[c] += 1
    return res

# I really like this solution
from collections import Counter

def count(string):
    return Counter(string)

print(count('aba'))