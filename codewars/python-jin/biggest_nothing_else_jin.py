# https://www.codewars.com/kata/631082840289bf000e95a334
def max_int_chain(n):
    if n < 5: return -1
    return (n//2)*(n//2 + 1) if n % 2 == 1 else (n//2 - 1) * (n//2 + 1)
print(max_int_chain(39))