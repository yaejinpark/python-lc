# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    new_num = []
    
    for i in range(a,b+1):
        digit_parser = [int(j) for j in str(i)]
        power = [digit_parser[j]**(j+1) for j in range(len(digit_parser))]
        
        if sum(power) == i:
            new_num.append(i)
    
    print(new_num)
    return new_num