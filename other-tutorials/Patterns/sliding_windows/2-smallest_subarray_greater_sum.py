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
	return min(output)
# Method above does not work because... 
# 1. I have to keep popping the subarray until the current window_sum's value is actually greater than 7 
# 2. Issue 1 can be fixed with another loop, but I have to be careful of the time complexity

# My attempt 2

def subarray_greater_sum2(arr,S):
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

		while window_sum >= S:
			output.append(len(subarray))
			subarray.pop(0)
			window_sum -= arr[window_start]
			window_start += 1
	return min(output)

# Issue: Doesn't take into account of a single element that is greater than or equal to S, test case 2 fail

# Better, and closer to the answer (better because less use of extra data structure)
def subarray_greater_sum3(arr,S):
	if len(arr) < 1: 
		return 0
	if len(arr) == 1 and arr[0] != S:
		return 0

	min_len = 999
	window_start = 0
	window_end = 0
	window_sum = 0.0

	for window_end in range(len(arr)):
		window_sum += arr[window_end]

		while window_sum >= S:
			min_len = min(min_len, window_end - window_start + 1) 
			# +1 is because the difference could be 0, which won't reflect the length of the array properly which could be 1 if start and end are the same.
			window_sum -= arr[window_start]
			window_start += 1
	if min_len == 999:
		return 0
	return min_len

sample_arr1 = [2, 1, 5, 2, 3, 2]
sample_arr2 = [2, 1, 5, 2, 8]
sample_arr3 = [3, 4, 1, 1, 6]

print(subarray_greater_sum3(sample_arr1,7)) # Should return 2
print(subarray_greater_sum3(sample_arr2,7)) # Should return 1
print(subarray_greater_sum3(sample_arr3,8)) # Should return 3
