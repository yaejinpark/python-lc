#If any element in a MxN matrix is a 0, its whole row and col should be zero
import random

def zeroMatrix():
    # matrix = createMatrix()
    matrix = [[8, 1, 4, 5, 5, 6, 8, 1],
              [4, 4, 6, 9, 3, 2, 6, 6],
              [0, 4, 1, 2, 7, 9, 9, 3],
              [4, 7, 0, 1, 1, 7, 1, 9]]


    print("Generated random matrix:", matrix)

    zeroRow, zeroCol = [],[]

    #For all values that are zero in the matrix, store their rows and values in two lists
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zeroRow.append(i)
                zeroCol.append(j)

    #For all values in the same row as 0's, change them to 0's as well
    for row in zeroRow:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0

    #For all values in the same col as 0's, change them to 0's as well
    for col in zeroCol:
        for row in range(len(matrix)):
            matrix[row][col]  = 0

    return(matrix)

#For generating a random MxN matrix with random values
def createMatrix():
    M = random.randint(1,9)
    N = random.randint(1,9)
    #Generate a matrix with M, N as any positive integer from 1-9
    #...with any positive integer values from 0 to 9
    matrix = [[random.randint(0,9) for val in range(M)] for val in range(N)]

    print("M:", M)
    print("N:", N)

    return matrix

print("Zero Matrix:", zeroMatrix())

#TL;DR
#If I store the coordinates of a 0 in two separate lists, it will be easier than dealing with tuples or nested list
#It's hard to find Java's nullifyRow/nullifyCol equivalent in python