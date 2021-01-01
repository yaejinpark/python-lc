#Tutorial from Brian Faure's YouTube Channel

from random import randint
def createArray(length=10, maxint=50):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

def bubbleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1],arr[i] = arr[i], arr[i-1]
                swapped = True
    return arr

arr = createArray()
print("array before sorting: ", arr)
arr = bubbleSort(arr)
print("array after sorting: ", arr)