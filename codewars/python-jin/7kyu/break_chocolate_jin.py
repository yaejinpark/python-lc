# https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python

def break_chocolate(n, m):
    # Return the minimum number of break offs into 1x1
    return n*m - 1 if n*m - 1 > 0 else 0