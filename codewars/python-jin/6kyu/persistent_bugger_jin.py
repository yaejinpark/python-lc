# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
def persistence(n):
    if n < 10:
        return 0
    product = 1
    for i in range(len(str(n))):
        product = product * int(str(n)[i])
    return 1 + persistence(product)