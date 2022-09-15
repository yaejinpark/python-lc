# https://www.codewars.com/kata/5904be220881cb68be00007d/train/python

def fish(shoal):
    exp_amount = 4 # starting level at 1 which is exp_level 4
    current_fish_size = 1
    if len(shoal) == 0 or shoal == '0': return 1 # if only algae or no shoals, return 1

    exp_total = {k:shoal.count(k)*int(k) for k in shoal}
    exp_one_shot = {'1':4,'2':12,'3':24,'4':40,'5':60,'6':84}
    
    for k,v in exp_total.items():
        if exp_one_shot[k] <= exp_amount:
            current_fish_size = k
        exp_amount += v
    
    return current_fish_size

1*(i-1)*4 + 4*(i)      i = 1
2*(i-1)*4 + 4*(i)      i = 2
3*(i-1)*4 + 4*(i)      i = 3