def firstDuplicate(a):
    duplicate = set()

    for i in a:
        if i in duplicate:
            return i
        duplicate.add(i)

    return -1

testArr = [2,1,3,5,3,2]
firstDuplicate(testArr)