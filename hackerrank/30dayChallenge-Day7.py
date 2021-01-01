#Print an array's contents backwards in a single line of string

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    string = arr[::-1]
    print(' '.join(map(str,string)))