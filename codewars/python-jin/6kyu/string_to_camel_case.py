# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
def to_camel_case(text):
    if len(text) == 0: return ""

    i = 0
    word = ""
    while i < len(text):
        if text[i] == "_" or text[i] == "-":
            word += text[i+1].upper()
            i += 1
        else:
            word += text[i]
        i += 1
    return word