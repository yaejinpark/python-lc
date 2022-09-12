# Question Link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

def solution(string, ending):
    # your code here...
    return ending in string[-len(ending):]