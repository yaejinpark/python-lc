# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def sq_in_rect(lng, wdth):    
    if lng == wdth: return None

    # biggest square size is the smaller of length and width
    squares = [min(lng,wdth)]
    bigger,smaller = max(lng,wdth), min(lng,wdth)
    new_square_size = 1

    # square_counter = bigger // smaller # for even
    # square_counter2 = bigger - smaller # for odd

    while new_square_size > 0:
        new_square_size = bigger % smaller
        frequency = bigger // smaller + 1
        squares.extend(frequency * [new_square_size])
        bigger = smaller
        smaller = new_square_size
        if smaller == 0:
            return squares

    print("[bigger, smaller]: ", [bigger,smaller])
    return squares

print(sq_in_rect(3,5)) # should be [3,2,1,1]
print(sq_in_rect(20,14)) # should be [14,6,6,2,2,2]