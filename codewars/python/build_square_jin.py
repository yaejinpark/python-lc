# Question Link: https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python

def generate_shape(n):
    initial = '+'*n + '\n'
    for i in range(n-1):
        initial += '+'*n + '\n'
    return initial[:-1]