# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
def is_valid_IP(strng):
    if len(strng) == 0: return False

    elems = strng.split(".")
    if len(elems) != 4: return False
    
    for elem in elems:
        if elem.isdigit():
            if int(elem) > 255:
                return False
            if elem[0] == '0' and len(elem) > 1:
                return False
        else:
            return False
    return True

# I like this one-liner
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))