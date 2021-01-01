def diagonalDifference(arr):
    ltr = 0
    rtl = 0

    halfway = int(len(arr) / 2)
    fullLen = len(arr) - 1

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (i == j):
                ltr += arr[i][j]
            if (i + j == fullLen):
                rtl += arr[i][j]

    print(abs(ltr - rtl))

    diagSum = abs(ltr - rtl)

    return diagSum