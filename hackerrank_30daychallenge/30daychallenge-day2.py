import math  

unit = 12

floa =  12.5
add = unit + floa

print(add)

print(math.ceil(add))
print(math.floor(add))

print(round(add))

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = meal_cost * tip_percent / 100
    tax_percent = meal_cost * tax_percent / 100
    total = meal_cost + tip_percent + tax_percent
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)



