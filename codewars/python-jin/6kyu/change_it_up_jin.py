# https://www.codewars.com/kata/58039f8efca342e4f0000023/train/python

def changer(s):
    char_shift = ""
    vowel = "aeiou"
    s = s.lower()
    for c in s:
        if c.isalpha() and c != 'z':
            char_shift += chr(ord(c) + 1)
        elif c == 'z':
            char_shift += 'a'
        else:
            char_shift += c
            
    res = "".join(c.upper() if c in vowel else c for c in char_shift)
    return res