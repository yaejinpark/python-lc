# Same problem as https://leetcode.com/problems/squares-of-a-sorted-array/

'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

'''
# Really tempting to use sorted()... let's try without for better time complexity

def solution(arr):
    i,j = 0, len(arr) - 1
    highest_index = j
    res = [0 for i in range(len(arr))]

    while i <= j:
        left = arr[i] ** 2
        right = arr[j] ** 2

        if left > right:
            res[highest_index] = left
            i += 1
        else:
            res[highest_index] = right
            j -= 1
        highest_index -= 1
    return res

arr1 = [-2,-1,0,2,3] 
arr2 = [-3,-1,0,1,2] 

print(solution(arr1)) # Should return [0,1,4,4,9]
print(solution(arr2)) # Should return [0,1,1,4,9]