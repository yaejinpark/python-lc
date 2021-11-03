def insertion_sort(arr):
	if len(arr) <= 1: # If there is one element or none in the array, return array as is
		return arr

	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
			print(f"Pairwise swap happening in while loop: {arr}")
		arr[j+1] = key
		print(f"End of a single for loop iteration: {arr}")

	return arr

test_arr = [5,2,4,6,1,3]
print(f"The original array was: {test_arr}")
print(f"The sorted array is: {insertion_sort(test_arr)}")