def create_array(size = 10, max = 100):

    from random import randint
    return [randint(0, max) for _ in range(size)]


def insertion_sort(arr): 

    if len(arr) <= 1:
        return arr 

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1 

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]

            j = j - 1 

        arr[j + 1] = key

    return arr 


def sorted_list():

    arr = create_array()

    print(f"Unsorted Array: {arr}")

    sort_arr = insertion_sort(arr)

    print(f"Sorted List: {sort_arr}")


sorted_list()