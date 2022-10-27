# https://www.codewars.com/kata/5ae326342f8cbc72220000d2/train/python
def string_expansion(s):
    if len(s) == 0 or s.isdigit(): return ""
    res = ""
    repeater = 1
    
    for c in s:
        if c.isdigit():
            repeater = int(c)
        else:
            res += repeater * c
    return res