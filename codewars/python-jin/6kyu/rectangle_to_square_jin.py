# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def sq_in_rect(lng, wdth):    
    if lng == wdth: return None
    
    sizes = []
    while lng and wdth:
        new_square_size = min(lng,wdth)
        sizes.append(new_square_size)
        if lng == new_square_size:
            wdth -= new_square_size
        else:
            lng -= new_square_size
    return sizes

print(sq_in_rect(3,5)) # should be [3,2,1,1]
print(sq_in_rect(20,14)) # should be [14,6,6,2,2,2]