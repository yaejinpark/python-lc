def merge(arr,l,m,r):
	n1 = m - l + 1 #n1 = 3 - 0 + 1 = 4
	n2 = r - m # n2 =  6 - 3 = 3

	# Create temp arrays
	L = [0] * n1 # Arrays of 0's with the length of n1 [0,0,0,0]
	R = [0] * n2 # Arrays of 0's with the length of n2 [0,0,0]

	# Copy data to temp arrays L[] and R[]
	for i in range(n1):
		L[i] = arr[l + i] # arr[0 + 0], arr[0 + 1], arr[0 + 2], arr[0 + 3] = 

	for j in range(n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0 # Initial index of first subarray
	j = 0 # Initial index of second subarray
	k = l # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
	    arr[k] = L[i]
	    i += 1
	    k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
	    arr[k] = R[j]
	    j += 1
	    k += 1

def mergeSort(arr,l,r):
	if l < r:
		m = l + (r-l) //2 
		# For L
		# 1st iteration: m = 3
		# 2nd iteration: m = 1
		# 3rd iteration: m = 0

		# For R
		# 1st iteration: m = 4
		# 2nd iteration: m = 5

		mergeSort(arr,l,m)
		print(f"Left Array: l={l}, m={m}") 
		# mergeSort(arr,0,3)
		# mergeSort(arr,0,1)

		mergeSort(arr,m+1,r)
		print(f"Right Array: l={m+1}, m={r}") 
		# mergeSort(arr,4,6)
		# mergeSort(arr,6,6)

		merge(arr,l,m,r)
		print(f"Merging: arr={arr}, l={l},m={m},r={r}")
		# merge(arr,0,3,6)


test_arr = [1,5,4,3,2,7,8] # length is 7, so the last index is 6

mergeSort(test_arr,0,6)