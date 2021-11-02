#Tutorial from Brian Faure's YouTube Channel

from random import randint
def createArray(length=10, maxint=50):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

def insertionSort(array):
    for sortedLen in range(1,len(array)):
        nextUnsortedItem = array[sortedLen]
        insertIndex = sortedLen

        while sortedLen > 0 and nextUnsortedItem < array[sortedLen]:
            array[sortedLen] = array[sortedLen-1]
            sortedLen -= 1

        array[insertIndex] = nextUnsortedItem

arr = createArray()
print("array before sorting: ", arr)
arr = insertionSort(arr)
print("array after sorting: ", arr)