"""
Given Input: 
	Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Find the average of all subarrays of K contiguous elements in a given array.

Expected Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""

# Brute Force (My attempt - no sliding windows)

def brute_force(arr,k):
	output = []

	for i in range(0,len(arr)):
		if i+k <= len(arr):
			elem_sum = 0
			for j in range(i,i+k):
				elem_sum += arr[j]
			output.append(elem_sum/k)
	return output


test_arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k_val = 5

print(brute_force(test_arr,k_val))

