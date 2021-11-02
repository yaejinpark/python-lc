def countSwaps(arr):
    numSwaps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                numSwaps += 1
                swapped = True
    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", arr[0])
    print("Last Element:", arr[len(arr) - 1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)