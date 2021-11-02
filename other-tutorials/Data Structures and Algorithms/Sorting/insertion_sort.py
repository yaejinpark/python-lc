def insertion_sort(arr):
	if len(arr) <= 1: # If there is one element or none in the array, return array as is
		return arr

	for i in range(1,len(arr)):
		value_to_sort = arr[i] # Otherwise known as 'key'

		while arr[i-1] > value_to_sort and i>0: # Conditions for pairwise swap to happen
			arr[i],arr[i-1] = arr[i-1],arr[i]
			i -= 1

	return arr

test_arr = [5,2,4,6,1,3]
print(f"The original array was: {test_arr}")
print(f"The sorted array is: {insertion_sort(test_arr)}")