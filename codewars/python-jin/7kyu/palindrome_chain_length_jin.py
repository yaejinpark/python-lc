# https://www.codewars.com/kata/525f039017c7cd0e1a000a26/python

def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    steps = 0
    num = n

    while str(num) != str(num)[::-1]:
        num = num + int(str(num)[::-1])
        steps += 1
    return steps

print(palindrome_chain_length(87))