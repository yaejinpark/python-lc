def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    sortedArr = sorted(arr)
    for i in range(0,len(sortedArr)-1):
        minSum += sortedArr[i]
    for i in range(1,len(sortedArr)):
        maxSum += sortedArr[i]
    print(minSum,maxSum)