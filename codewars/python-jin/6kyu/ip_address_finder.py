# https://www.codewars.com/kata/5b883cdecc7c03c0fa00015a/train/python
def f(u):return [i*sum(map(ord,u))%256 for i in range(1,5)]