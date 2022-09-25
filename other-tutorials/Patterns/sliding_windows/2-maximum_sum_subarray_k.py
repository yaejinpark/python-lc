"""
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""

def max_sum(arr,k):
    if len(arr) < k: return sum(arr)
    max_sum = -999
    i,j = 0,k

    while j < len(arr):
        if sum(arr[i:j]) > max_sum:
            max_sum = sum(arr[i:j])
        i += 1
        j += 1
    return max_sum