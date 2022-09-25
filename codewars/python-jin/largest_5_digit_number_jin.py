# https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python

def solution(digits):
    i,j = 0,5
    max_digits = 0
    
    while j-1 < len(digits):
        if int(digits[i:j]) > max_digits:
            max_digits = int(digits[i:j])
        i += 1
        j += 1
    return max_digits