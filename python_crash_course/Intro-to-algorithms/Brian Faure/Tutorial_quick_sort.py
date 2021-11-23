from random import randint
from typing import Sized


def create_array(size =10, max = 100): 
    from random import randint
    return[randint(0, max) for _ in range(size)]

def quick_sort(array):

    if len(array) <= 1: 
        return array

    smaller, equal, larger = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for x in array: 
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)


def sorted_list(): 

    array = create_array()

    print(f"Unsorted Array: {array}")

    sort_list = quick_sort(array)

    print(f"Sorted List: {sort_list}")


sorted_list()