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
# My attempt
def subarray_greater_sum(arr,S):
	if len(arr) < 1: 
		return 0
	if len(arr) == 1 and arr[0] != S:
		return 0

	output,subarray = [],[]
	shortest_len = 100000
	window_start, window_sum = 0, 0.0

	for window_end in range(0,len(arr)):
		subarray.append(arr[window_end])
		window_sum += arr[window_end]

		if window_sum >= S:
			# print(subarray)
			output.append(len(subarray))
			subarray.pop(0)
			window_sum -= arr[window_start]
			window_start += 1
# Method above does not work because... 
# 1. I have to keep popping the subarray until the current window_sum's value is actually greater than 7 
# 2. Issue 1 can be fixed with another loop, but nested loop defeats the purpose of having a window.


sample_arr1 = [2, 1, 5, 2, 3, 2]
sample_arr2 = [2, 1, 5, 2, 8]
sample_arr3 = [3, 4, 1, 1, 6]

subarray_greater_sum(sample_arr1,7)
print(subarray_greater_sum(sample_arr1,7)) # Should return 2
# subarray_greater_sum(sample_arr2,7) == 1 # Should return 1
# subarray_greater_sum(sample_arr3,8) == 3 # Should return 3
