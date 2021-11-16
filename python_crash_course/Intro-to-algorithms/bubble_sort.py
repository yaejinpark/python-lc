from typing import List


def create_array(size = 10, max = 50): 
    from random import randint
    return [randint(0, max) for _ in range(size)]

def my_try(arr): 

    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i - 1 

        while key >= 1 and key < arr[j]:
            arr[j + 1] = key
            j += 1

        key = arr[i + 1]

        

        return arr 




def bubble_sort(arr): 

    n = len(arr)
    iteration = 0 
    for i in range(n): 

        for j in range(0, n - i - 1): 

            

            if arr[j] > arr[j + 1]: 
                
                
                arr[j], arr[j + 1 ] = arr[j + 1], arr[j]
                

            else: 
                arr
            
            print(f"Step:{iteration}. The array is: {arr}")
            
            iteration += 1

    return arr 



 
def sorted_list():

    arr = create_array()
    print(f"Unsorted Array: {arr}")

    sort_list = bubble_sort(arr)

    print(f"Sorted Array: {sort_list}")

sorted_list()


haas = [1, 2 ,4 ,5 , 24, 242]

n = len(haas)

print(len(haas))

print(range(n))