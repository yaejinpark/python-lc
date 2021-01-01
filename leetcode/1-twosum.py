def twoSum(nums, target):
    i = 0

    valueDict = {}
    for i, num in enumerate(nums):
        #i will later be the index number for the returned array
        #iterates through (i, num)
        print(i, num)
        if target - num in valueDict:
            return (valueDict[target - num], i)
        valueDict[num] = i

testArray = [3,2,4]
testTarget = 6
print(twoSum(testArray,testTarget))
