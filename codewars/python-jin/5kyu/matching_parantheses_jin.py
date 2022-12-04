# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
import re
def valid_parentheses(string):
    try:
        re.compile(string)
        return True
    except: return False

# Without using regex
def valid_parentheses(string):
    counter = 0
    for i in [*string]:
        if i == "(" and counter >= 0:
            counter += 1
        elif i == ")":
            counter -= 1
        else:
            pass
    if counter == 0:
        return True
    else:
        return False

valid_parentheses("hi()()")
valid_parentheses("()()()")