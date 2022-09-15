# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
def in_array(array1, array2):
    # your code
    r = []
    
    new_a2 = ','.join(array2)
    for word in array1:
        if word in new_a2:
            r.append(word)
    return sorted(set(r))