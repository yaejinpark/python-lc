# https://www.codewars.com/kata/5469e0798a3502f4a90005c9/train/python

def rotate(data, n):
    if len(data) == 0: return []
    n = n % len(data)
    return data[-n:] + data[:-n]