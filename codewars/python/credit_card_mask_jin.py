# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
def maskify(cc):
    return '#' * len(cc[:len(cc) - 4]) + cc[len(cc) - 5 + 1:] if len(cc) > 4 else cc