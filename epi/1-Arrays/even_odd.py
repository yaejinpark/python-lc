# Reorder array entries so that even entries appear first
from random_arrays import create_positive_array as cpa

def even_odd(arr):
    print("Original Array:",arr)
    next_even,next_odd = 0,len(arr)-1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even],arr[next_odd] = arr[next_odd],arr[next_even]
            next_even += 1
            next_odd -= 1
    print("Sorted Array:",arr)
    return arr

arr = cpa()
even_odd(arr)
