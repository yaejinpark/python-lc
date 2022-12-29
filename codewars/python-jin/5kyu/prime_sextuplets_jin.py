# https://www.codewars.com/kata/57bf7fae3b3164dcac000352/train/python
from gmpy2 import is_prime,next_prime

def find_primes_sextuplet(sum_limit):
    i = (sum_limit-30)//6
    while True:
        candidates = [i,i+4,i+6,i+10,i+12,i+16]
        if all(is_prime(j) for j in candidates):
            if sum(candidates) > sum_limit:
                return candidates
        i = next_prime(i)