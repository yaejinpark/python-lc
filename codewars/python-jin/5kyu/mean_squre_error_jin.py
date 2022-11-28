# https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python
def solution(array_a, array_b):
    return sum([(array_a[i] - array_b[i]**2) for i in range(len(array_a))])/len(array_a)