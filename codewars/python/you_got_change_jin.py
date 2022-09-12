# https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/python
def give_change(amount): 
    change_list = {1:0,5:0,10:0,20:0,50:0,100:0}
    bills_list = [1,5,10,20,50,100]
    
    while amount > 0:
        max_bill = max(bills_list)
        if amount >= max_bill:
            change_list[max_bill] += 1
            amount -= max_bill
        if amount % max_bill == amount:
            bills_list.remove(max_bill)
    return tuple([v for k,v in change_list.items()])