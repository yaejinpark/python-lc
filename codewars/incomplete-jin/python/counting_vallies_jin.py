# https://www.codewars.com/kata/5da9973d06119a000e604cb6/train/python

def counting_valleys(s):
    levels = [-1 if c == 'D' else 0 if c == 'F' else 1 for c in s]
    entered_valley = False
    exited_valley = False
    valley_counter = 0
    
    i,j = 0,1
    
    while i < len(levels):
        if levels[i] > 0 and levels[j] == -1:
            entered_valley = True
            j += 1
        if levels[j] > levels[i] and entered_valley:
            exited_valley = True
            valley_counter += 0
        i += 1
    return valley_counter
    