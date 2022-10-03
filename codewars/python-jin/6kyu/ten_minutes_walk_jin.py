# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    return False if len(walk) != 10 else walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')