def hourglassSum(arr):
    maxSum = -10000000
    findSum = 0

    for i in range(1, 5):
        for j in range(1, 5):
            findSum = arr[i][j] + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i + 1][j - 1] + \
                      arr[i + 1][j] + arr[i + 1][j + 1]
            if findSum > maxSum:
                maxSum = findSum

    return maxSum