# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    # your code
    int_str = str(n)
    int_str_list = [int(i) for i in int_str]
    powers = [p + i for i in range(0,len(int_str_list))]
    
    total_sum = sum([i[0]**i[1] for i in zip(int_str_list,powers)])
    
    k = total_sum/n
    
    return k if k.is_integer() else -1