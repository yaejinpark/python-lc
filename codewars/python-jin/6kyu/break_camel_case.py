# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
def solution(s):
    i = 0
    word = ""
    
    while i < len(s):
        if s[i].isupper():
            word += " "
        word += s[i]
        i += 1
    return word

# Someone's one liner I liked
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)