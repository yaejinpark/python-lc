import random

def create_positive_array():
    arr = [];
    len = random.randint(2,10); # Randomize length of array

    for i in range(0,len):
        arr.append(random.randint(1,9))
    return arr
