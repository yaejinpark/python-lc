# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python

def power_sumDigTerm(n):
    num_list = []
    for i in range(3,100):
        for j in range(2,100):
            power = i**j
            num = sum([int(x) for x in str(power)])
            if i == num:
                num_list.append(power)
                
    num_list.sort()
    
    return num_list[n-1] if n >= 1 else num_list[0]