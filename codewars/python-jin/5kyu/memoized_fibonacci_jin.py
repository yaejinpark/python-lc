# https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python
fib_dict = {}

def fibonacci(n):
    if n in [0,1]: return n
    elif n in fib_dict: return fib_dict[n]
    else:
        val = fibonacci(n-1) + fibonacci(n-2)
        fib_dict[n] = val
    return val