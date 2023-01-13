# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

def remove_parentheses(s):
    i,res = 0,''
    
    for c in s:
        if c == '(': i += 1
        if i == 0: res += c
        if c == ')': i -= 1
    return res