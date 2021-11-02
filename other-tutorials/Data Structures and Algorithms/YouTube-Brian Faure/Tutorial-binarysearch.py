#Tutorial from Brian Faure's YouTube Channel
#Search the input array arr for a specific value val

def binarySearch(arr,val):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
        return False

    mid = arr[len(arr)/2]

    #case 1: val is same as mid, return True
    if val == mid:
        return True

    #case 2: if val is greater than mid, chop off left of array
    if val > mid:
        return binarySearch(arr[len(arr)/2+1:], val)

    #case 3: if val is smaller than mid, chop off right of array
    if val < mid:
        return binarySearch(arr[:len(arr)/2], val)



testList = [1,2,3,4,5,6,7,8,9]
#Should print False
print(binarySearch(testList,0))
#Should print True
print(binarySearch(testList,8))