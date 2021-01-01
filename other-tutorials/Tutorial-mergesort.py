#Tutorial from Brian Faure's YouTube Channel

from random import randint

def createArray(length=10, maxint=50):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

def merge(arr1,arr2):
    index1 = 0
    index2 = 0
    mergedArray = []

    while index1<len(arr1) and index2<len(arr2):
        if arr1[index1] < arr2[index2]:
            mergedArray.append(arr1[index1])
            index1 += 1
        else:
            mergedArray.append(arr2[index2])
            index2 += 1

    if index1 == len(arr1):
        mergedArray.extend(arr2[index2:])
    else:
        mergedArray.extend(arr1[index1:])

    return mergedArray

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    left,right = mergeSort(arr[len(arr)/2:]), mergeSort(arr[:len(arr)/2])
    return merge(left,right)

arr1 = createArray()
print("arr1: ", arr1)
arr2 = createArray()
print("arr2: ", arr2)
merged = merge(arr1,arr2)
print("arr1 and arr2 merged: ", merged)
print("after merge sort: ", mergeSort(merged))
