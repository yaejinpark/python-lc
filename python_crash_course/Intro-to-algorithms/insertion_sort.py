def create_array(size = 10, max = 50): 
    from random import randint
    return [randint(0, max) for _ in range(size)]

def insertion_sort(arr):

    for i in range(0, len(arr)):

        key = arr[i] 

        j = i -1 

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]

            j = j - 1 

        arr[j + 1] = key 
    
    return arr

arr = create_array()

print(list)

sorted_arr = insertion_sort(arr)

print(sorted_arr)
