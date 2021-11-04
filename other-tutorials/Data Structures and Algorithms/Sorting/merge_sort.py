# Import random integer array class file
import sys
sys.path.append('..')
from random_integer_arrays import IntegerArray

# This function is where the arrays get merged when called
def merge(left_arr,right_arr):
	res = []

	left_pointer, right_pointer = 0,0

	# After comparing values in each array, append the smaller value into the res array
	# And increment the pointer of the array where the smaller value came from
	while left_pointer < len(left_arr) and right_pointer < len(right_arr):
		if left_arr[left_pointer] < right_arr[right_pointer]:
			res.append(left_arr[left_pointer])
			left_pointer += 1
		else:
			res.append(right_arr[right_pointer])
			right_pointer += 1

	# Append (extend) any remaining values in the longer half of the array
	res.extend(left_arr[left_pointer:])
	res.extend(right_arr[right_pointer:])

	return res

# This is where the arrays get separated into individual elements and calls the merge function
def merge_sort(arr):
	# Partition array until each element are in their separate arrays
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2

	# Partition happening with updated mid
	left_arr,right_arr = merge_sort(arr[:mid]),merge_sort(arr[mid:])
	merged = merge(left_arr,right_arr)

	# print(f"merge_sort left array: {left_arr}")
	# print(f"merge_sort right array: {right_arr}")
	# print(f"merged arrays: {merged}")

	return merged


testArray1 = IntegerArray(5,10).create_array()
testArray2 = IntegerArray(8,20).create_array()
testArray3 = IntegerArray(1,3).create_array()
print(f"Original array: {testArray1}")
print(f"Merge sorted array: {merge_sort(testArray1)}")
print(f"Original array: {testArray2}")
print(f"Merge sorted array: {merge_sort(testArray2)}")
print(f"Original array: {testArray3}")
print(f"Merge sorted array: {merge_sort(testArray3)}")
