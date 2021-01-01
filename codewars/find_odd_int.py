#Given an array, find the integer that appears an odd number of times.

def find_it(seq):

    for num in seq:
        if seq.count(num) % 2 == 1:
            print(num)
            return num
        else:
            pass


testarray1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
testarray2 = [1,1,2,-2,5,2,4,4,-1,-2,5]
testarray3 = [20,1,1,2,2,3,3,5,5,4,20,4,5]

find_it(testarray1)