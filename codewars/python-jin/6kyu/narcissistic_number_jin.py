# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic( value ):
    str_val = str(value)
    return value == sum(int(c)**len(str_val) for c in str_val)