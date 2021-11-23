# QUICK SORT 
from random import randint

def create_array(size=10, max = 50): 
    
    return [randint(0, max) for _ in range(size)]


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

    print("\nQUICK SORT ALGORITHM")

    arr = create_array()

    print(f"Unsorted Array: {arr}")

    sort_list = quick_sort(arr)

    print(f"Sorted List: {sort_list}")

sorted_list()