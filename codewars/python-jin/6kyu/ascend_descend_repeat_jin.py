# https://www.codewars.com/kata/62ca07aaedc75c88fb95ee2f/train/python

def ascend_descend(length, minimum, maximum):
    min_max = [i for i in range(minimum,maximum+1)]
    max_min = [i for i in range(maximum-1,minimum-1,-1)]
    seq = min_max + max_min
    res = ''
    
    if(len(seq)) <= 1:
        res = ''.join([str(i) for i in seq])*length
    else:
        res = ''.join([str(i) for i in seq[:-1]])*length
    
    return res[:length]