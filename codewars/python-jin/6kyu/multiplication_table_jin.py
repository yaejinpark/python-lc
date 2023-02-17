# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
def multiplication_table(size):
    res = []
    for i in range(1,size+1):
        dummy = []
        for j in range(1,size+1):
            dummy.append(i*j)
        res.append(dummy)
    return res