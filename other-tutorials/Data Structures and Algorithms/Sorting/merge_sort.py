# Practice based on Brian Faure's video

# Import random integer array class file
import sys
sys.path.append('..')
from random_integer_arrays import IntegerArray

# This function is where the arrays get merged when called
def merge(left_arr,right_arr):
	res = []



	return res

# This is where the arrays get separated into individual elements and calls the merge function
def merge_sort(arr):
	# Partition array until each element are in their separate arrays
	if len(arr) <= 1:
		return arr

	mid = len(arr)//2

	# Partition happening with updated mid
	left_arr,right_arr = merge_sort(arr[:mid]),merge_sort(arr[mid+1:])
	merged = merge(left_arr,right_arr)

	print(f"merge_sort left array: {left_arr}")
	print(f"merge_sort right array: {right_arr}")
	print(f"merged arrays: {merged}")

	return merged


testArray1 = IntegerArray(5,10).create_array()
testArray2 = IntegerArray(8,20).create_array()
testArray3 = IntegerArray(1,3).create_array()
print(testArray1)
print(testArray2)
print(testArray3)
