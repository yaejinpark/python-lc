def rotateImage(a):
    print(list(zip(*a[::-1])))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateImage(matrix)