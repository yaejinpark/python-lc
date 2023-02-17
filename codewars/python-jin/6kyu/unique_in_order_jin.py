# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    if len(sequence) == 1: return list(sequence)
    if len(sequence) == 0: return []

    res,i = [sequence[0]],0
        
    while i + 1 < len(sequence):
        if sequence[i] != sequence[i+1]:
            res.append(sequence[i+1])
        i += 1

    return res