# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    if len(str(n)) == 1:
        return n
    current_sum = sum([int(i) for i in str(n)])
    return digital_root(current_sum)