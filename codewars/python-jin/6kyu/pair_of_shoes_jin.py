# https://www.codewars.com/kata/58885a7bf06a3d466e0000e3/train/python
def pair_of_shoes(shoes):
    left = sorted([size for lr,size in shoes if lr==1])
    right = sorted([size for lr, size in shoes if lr==0])
    return left == right

# Or... one liner
def pair_of_shoes(shoes):
    return sorted([size for lr,size in shoes if lr==1]) == sorted([size for lr, size in shoes if lr==0])