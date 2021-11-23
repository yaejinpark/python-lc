# FIRST ALGORITHMIC SORTING METHOD (INSERTION SORT)

# Insortion sort is a sorting algorithm where the list is divided into a sorted
# and unsorted side. The list gets sorted form left to right, individually 
# comparing the values in the sorted (left side) with the fist value in the 
# unsorted side (right side). The worst case time complexity for this method is O(n2)
# and the best case is O(n)

# Create a random arry function
from os import O_TRUNC
from random import randint


def create_array(size = 10, max = 100):

    from random import randint
    return [randint(0, max) for _ in range(size)]




# Insertion sort function
def insertion_sort(arr): 

    # Check whether or not the list is empty or equal to one
    if len(arr) <= 1: 
        return arr

    for i in range(1, len(arr)):
        key = arr[i]

        j = i -1 

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]

            j = j - 1 

        arr[j + 1] = key 

    return arr 


# Print random arry sorted as a function 
def sorted_list(): 

    print("\nINSERTION SORT ALGORITHM")

    arr = create_array()

    print(f"Unsorted List: {arr}")

    sort_list = insertion_sort(arr)

    print(f"Sorted List: {arr}\n")


sorted_list()


#  SECOND ALGORITHMIC SORTING METHOD - MERGE SORT 

# Merge sort is a recursive divide - conquer sorting algorithm where the values 
# in an array are divided until they are individually separated. Afterwards the
# values are compared against each other building the array back in numerical order 
# The best and worst case time complexity for this algorithm is O(nlog n)

# Merge Sort 

# I'll write this algorithm in two functions. The merge function will merge the 
# right array with the left array. The merge sort function will sort the array
# recursively. 

def merge_sort(right, left): 

   

    result = []
    
    r, l = 0 , 0 

    while r < len(right) and l < len(left): 
        if right[r] > left[l]:
            result.append(left[l])
            l += 1
        
        else:
            result.append(right[r])
            r += 1 

    result.extend(right[r:])
    result.extend(left[l:])

    return result







def merge(arr): 

    # Check whether or not the list is empty or equal to one
    if len(arr) <= 1: 
        return arr 

    mid = len(arr) // 2

    right = merge(arr[mid:])
    left = merge(arr[:mid])

    return merge_sort(right, left)


def sorted_list(): 

    print("\nMERGE SORT ALGORITHM")

    arr = create_array()

    print(f"Unsorted Array: {arr}")

    sort_list = merge(arr)

    print(f"Sorted List: {sort_list}")


sorted_list()



# THIRD ALGORITHMIC SORTING METHOD - BUBBLE SORT 

# In this sorting method starting from the left each adjacent value 
# is compared with the value on the right. Swapping if the left value is bigger than 
# the right 



def bubble_sort(arr): 

    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 


def sorted_list(): 

    print("\nBUBBLE SORT ALGORITHM")

    arr = create_array()

    print(f"Unsorted Array: {arr}")

    sort_list = bubble_sort(arr)

    print(f"Sorted List: {sort_list}")


sorted_list()


# FORTH ALGORITHMIC SORTING METHOD - QUICK SORT 

# This is also a divide and conquer sorting algorithm. In this sorting algorithm 
# we select a pivot value that can be used to compare and swap smaller values to 
#it's left and bigger values to it's right. 


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
