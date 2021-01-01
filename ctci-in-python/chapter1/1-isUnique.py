def isUnique(testString):
    dict = {}
    for i in range(0,len(testString)):
        if testString[i] not in dict:
            dict.update({testString[i]:1})
        else:
            dict[testString[i]] += 1
    print(dict)

    for nums in dict:
        if dict.get(nums) > 1:
            return False
        else:
            return True

testString1 = "abcdefghi"
testString2 = "abcdea"
testString3 = "aaaabcd"
# print(isUnique(testString3))

#Notes after checking solution
#1. I don't have to store the frequency of the letters. If it's duplicate, it's done.
#2. Then I can just use boolean. If it appeared once already, isUnique returns False.
#3. Storing data is wasting memory in this case.

#Second Attempt

def isUnique2(testString):
    dict = {}
    for char in testString:
        #if duplicate found, return False
        if char in dict:
            return False
        dict[char] = True
    return True

print(isUnique2(testString1))
print(isUnique2(testString2))

#TL;DR
#Dictionary is useful, but remember that I can also set the keys' values as booleans
#For challenges that checks for unique whatevers, boolean is enough because an element is either unique or not.