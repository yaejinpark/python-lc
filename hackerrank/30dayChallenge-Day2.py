import math

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    total = meal_cost+tip+tax

    if ((total - math.floor(total)) >= 0.5):
        total = math.ceil(total)
        print (total)
    else:
        print (total)


solve(10.25, 17, 5)