"""
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.
----------------------------------------------------------------------------------------------
Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].
----------------------------------------------------------------------------------------------
"""
def subarray_greater_sum(arr,s):
	min_len = 0
	current_len = min_len
	current_sum = 0
	i,j = 0,len(arr)-1

	while i < len(arr):
		if sum(arr[i:j]) >= s:
			current_len = len(arr[i:j+1])
			if current_len < min_len:
				min_len = current_len
		i += 1
	print(arr[i:j])
	return min_len

sample_arr1 = [2, 1, 5, 2, 3, 2]
sample_arr2 = [2, 1, 5, 2, 8]
sample_arr3 = [3, 4, 1, 1, 6]

print(subarray_greater_sum(sample_arr1,7)) # Should return 2
print(subarray_greater_sum(sample_arr2,7)) # Should return 1
print(subarray_greater_sum(sample_arr3,8)) # Should return 3
