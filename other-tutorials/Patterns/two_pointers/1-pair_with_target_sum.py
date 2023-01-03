# Same problem as TwoSum on Leetcode
"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

# Brute Force - Attempt 1
def target_sum(arr,target):
	res = []
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i] + arr[j] == target:
				res.append(i)
				res.append(j)
	return res

# The time complexity of this algorithm will be O(N*logN). Can we do better than this?

# Attempt 2 - Can I do better? Hint: Use the fact that the array is sorted.

def target_sum2(arr,target):
	start, end = 0, len(arr) - 1

	while start < end:
		current_sum = arr[start] + arr[end]

		if current_sum == target:
			return [start,end]
		if current_sum > target:
			end -= 1
		elif current_sum < target:
			start += 1
	return [-1,-1]

"""
Time Complexity:

The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.

Space Complexity:

The algorithm runs in constant space O(1).

"""
# Two pointer way - How I should really do it to minimize space complexity
def target_sum3(arr,target):
	i = 0
	j = len(arr) - 1 

	while i < j:
		current_sum = arr[i] + arr[j]
		if current_sum == target:
			return [i,j]
		elif current_sum < target:
			i += 1
		else:
			j -= 1
	return False

# Alternate way - Use Hashmaps

def target_sum4(arr,target):
	value_dict = {}
	for i,val in enumerate(arr):
		if target - val in value_dict:
			return [value_dict[target-val],i]
		value_dict[val] = i
	return value_dict

arr1 = [1,2,3,4,6]
arr2 = [2,5,9,11]

print(target_sum3(arr1,6)) # Should return [1,3]
print(target_sum3(arr2,11)) # Should return [0,2]
