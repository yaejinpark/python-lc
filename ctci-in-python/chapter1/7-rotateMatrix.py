#Assume it's 90 degrees rotation to the right
# [[0 1 2]     [[6 3 0]
#  [3 4 5]   -> [7 4 1]
#  [6 7 8]]     [8 5 2]]

def rotate(mat):
    print(list(zip(*mat[::-1])))

test = [[0,1,2],[3,4,5],[6,7,8]]

rotate(test)

#TL;DR
# * unpacks the list
# [::-1] makes a copy of the original list in a reverse order
# zip() takes one item from each list (row, in this case) and makes a tuple

# [[0 1 2]         [[6 7 8] (::-1)       [[6 3 0]   (zip)
#  [3 4 5]   ->     [3 4 5]       ->      [7 4 1]
#  [6 7 8]]         [0 1 2]]              [8 5 2]]
