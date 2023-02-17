# Similar to Leetcode's 3Sum

'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

'''
def find_pairs(arr,i,target):
    j = len(arr)-1
    triplets = []
    while i < j:
        if arr[i] + arr[j] == target:
            triplets.append([-target,arr[i],arr[j]])
            i += 1
            j -= 1
            while i < j and arr[i] == arr[i - 1]: # Avoiding duplicates on the left side
                i += 1
            while i < j and arr[j] == arr[j+1]: # Avoiding duplicates on the right side
                j -= 1
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1
    return triplets

def solution(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        dummy = find_pairs(arr,i+1,-arr[i])
        if dummy:
            res.extend(dummy)
    return res

test_arr1 = [-3, 0, 1, 2, -1, 1, -2]
test_arr2 = [-5, 2, -1, -2, 3]
print(solution(test_arr1))