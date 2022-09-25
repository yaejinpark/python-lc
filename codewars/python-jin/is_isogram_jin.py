# Question Link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    return len(set(string.lower())) == len(string.lower())