# https://www.codewars.com/kata/582dcda401f9ccb4f0000025/train/python
from gmpy2 import next_prime

def even_counter(x):
    nums = [int(i) for i in str(x)]
    counter = 0
    for num in nums:
        if num % 2 == 0:
            counter += 1
    return counter

def f(n):
    current_prime = 2
    max_even = 1
    winning_num = 0
    
    while current_prime < n:
        even_count = even_counter(current_prime)
        if even_count >= max_even:
            max_even = even_count
            winning_num = current_prime
        current_prime = next_prime(current_prime)
    return winning_num