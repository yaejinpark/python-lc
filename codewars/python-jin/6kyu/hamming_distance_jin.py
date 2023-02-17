# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python
def hamming(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter