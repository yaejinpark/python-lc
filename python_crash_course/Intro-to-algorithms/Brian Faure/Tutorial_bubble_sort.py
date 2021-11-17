def create_array(size = 10, max = 50): 
    from random import randint
    return [randint(0, max) for _ in range(size)]


def bubble_sort(arr): 

    swapped = True 

    while swapped:
        swapped = False

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
    
    return arr


def sorted_list():

    arr = create_array()
    print(f"Unsorted Array: {arr}")

    sort_list = bubble_sort(arr)

    print(f"Sorted Array: {sort_list}")

sorted_list()
