# https://www.codewars.com/kata/56f78a42f749ba513b00037f/train/python
import itertools

def rolldice_sum_prob(sum_, dice_amount):    
    all_rolls = 6 ** dice_amount
    
    if sum_ > 6*dice_amount or sum_ < 1*dice_amount: return 0

    a = [c for c in itertools.product([1,2,3,4,5,6], repeat=dice_amount)]
        
    counter = 0
    for combo in a:
        if sum(combo) == sum_:
            counter += 1
    
    return counter/len(a)