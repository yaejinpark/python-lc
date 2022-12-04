# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(lst):
    j = 0
    
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i],lst[j] = lst[j],lst[i]
            j += 1
    return lst