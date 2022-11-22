# https://www.codewars.com/kata/5314b3c6bb244a48ab00076c/train/python
def luck_check(string):
    if any(c.isalpha() for c in string): raise ValueError
    half = len(string)//2 
    sum1 = sum([int(i) for i in string[:half]])
    sum2 = sum([int(i) for i in string[half:]]) if len(string) % 2 == 0 else sum([int(i) for i in string[half+1:]])
    return sum1 == sum2