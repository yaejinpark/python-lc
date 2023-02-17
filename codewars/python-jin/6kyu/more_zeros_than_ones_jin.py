# https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python
def more_zeros(s):
    non_duplicate = ''.join([j for i,j in enumerate(s) if j not in s[:i]]) # get unique strings in the same order as original string
    res = []
    for c in non_duplicate:
        to_bin = bin(ord(c))[2:]
        if to_bin.count('1') < to_bin.count('0'):
            res.append(c)
    return res