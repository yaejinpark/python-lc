# https://www.codewars.com/kata/55de8eabd9bef5205e0000ba/train/python

from gmpy2 import is_prime

def find_emirp(n):
    emirps = []
    for i in range(13,n+1,2):
        flipped = int(str(i)[::-1])
        if is_prime(i) and is_prime(flipped) and str(i) != str(i)[::-1]:
            emirps.append(i)
    
    return [len(emirps),max(emirps),sum(emirps)] if emirps else [0,0,0]