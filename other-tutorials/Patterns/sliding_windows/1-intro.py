"""
Given Input: 
	Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Find the average of all subarrays of K contiguous elements in a given array.

Expected Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""

# Brute Force (My attempt - no sliding windows), Time Complexity of O(N*k)

def brute_force(arr,k):
	output = []

	for i in range(0,len(arr)):
		if i+k <= len(arr):
			elem_sum = 0
			for j in range(i,i+k):
				elem_sum += arr[j]
			output.append(elem_sum/k)
	return output

# Better way - consider the subarrays as windows, add/subtract windows and reuse the sum of 4 overlapping elements.

def windows_avg(arr,k):
	output = []
	window_start,window_sum = 0, 0.0

	for window_end in range(len(arr)):
		window_sum += arr[window_end]

		if window_end >= k-1: # window_end starts at 0, so just having it = k will make the sum have sum of 6 elements
			output.append(window_sum/k)
			window_sum -= arr[window_start]
			window_start += 1 # start of the window shifts by 1
	return output


test_arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k_val = 5

# print(brute_force(test_arr,k_val))
print(windows_avg(test_arr,k_val))

