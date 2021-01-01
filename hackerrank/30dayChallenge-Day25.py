#Determine if a number is prime or not
import math


def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, int(math.ceil(math.sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True


getInput = int(input())

for _ in range(getInput):
    num = int(input())

    if isPrime(num):
        print("Prime")
    else:
        print("Not prime")