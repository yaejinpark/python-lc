# Question Link: https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    #good luck!
    if a == b:
        return a

    return sum([i for i in range(min(a,b),max(a,b)+1)])