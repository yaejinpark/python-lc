def create_array(size = 1, max = 20): 
    from random import randint 

    return [randint(0, max) for _ in range(size)]


def insertion_sort(arr): 

    if len(arr) <= 1: 
        return arr 

    for i in range(0, len(arr)): 

        key = arr[i]
        j = i - 1 

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr 





arr = create_array()

print(f"Unsorted Array: {arr}")

sorted_arr = insertion_sort(arr)

print(f"Sorted List: {sorted_arr}")