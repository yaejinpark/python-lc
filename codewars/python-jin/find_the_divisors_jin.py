# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
def divisors(integer):
    divisors = []
    for i in range(integer-1,0,-1):
        if integer % i == 0 and i != 1:
            divisors.append(i)
    return str(integer) + ' is prime' if len(divisors) == 0 else divisors[::-1]