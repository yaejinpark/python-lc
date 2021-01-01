#A string can have a character inserted, removed, or replaced
#Find if a string is one or no edits away from another string.

def oneWay(string1, string2):
    if len(string1) - len(string2) > 1:
        print("More than one edit away!")
        return False

    originalString = {}
    editCounter = 0

    for char in string1:
        if char not in originalString:
            originalString[char] = True

    #If there two strings length difference is 1, add to editCounter
    if len(string1) - len(string2) == 1:
        editCounter += 1

    #For every different letter in string 2, add to the editCounter
    for char in string2:
        if char not in originalString:
            editCounter += 1

    if editCounter < 2:
        return True
    else:
        print("More than one edit. Total edit counter: ", editCounter)
        return False

# test1 = "cat"
# test2 = "tca"
# print(oneWay(test1,test2))

#The method above is wrong because cat and tca are at least 2 edits away from each other.
#But if I use a dictionary, it doesn't care about the order of the letters of each string.
#Let's try again WITHOUT using a dictionary.

def oneWay2(string1, string2):
    editCounter = 0

    #If both strings have the same length, count the number of different letters
    if len(string1) == len(string2):
        for i in range(len(string2)):
            if string2[i] != string1[i]:
                editCounter += 1
                if editCounter > 1:
                    print("Same Lengths. More than one edit:", editCounter)
                    return False
        print("Edit Counter:", editCounter)
        return True

    #do a comparison on both strings that have different lengths
    shortString = ""
    longString = ""
    if abs(len(string1) - len(string2)) == 1:
        if len(string1) < len(string2):
            shortString,longString = string1, string2
        else:
            shortString,longString = string2, string1

        i = 0
        j = i
        shift = 0
        while i < len(longString) and j < len(shortString):
            #If char in both string are different, shift the pointer in the longer string by the amount of difference
            if shortString[j] != longString[i]:
                editCounter += 1
                shift += 1
                i = j + shift
            #If both characters are the same, move onto the next character
            elif shortString[j] == longString[i]:
                shift = 0
                j += 1
                i += 1
            if editCounter > 1:
                print("Different Lengths. More than one edit:", editCounter)
                return False
        print("Edit Counter:",editCounter)
        return True

    else:
        print("More than one edit!")
        return False

test1 = "cat"
test2 = "tca"
test3 = "pale"
test4 = "bale"
test5 = "coffee"
test6 = "covfefe"
print(oneWay2(test1,test2))
print("\n")
print(oneWay2(test3,test4))
print("\n")
#For this test, change line 76 to editCounter > 3
print(oneWay2(test5,test6))

#TL;DR
#Sometimes, dictionary is not the answer. Surprise.
#Keeping a counter variable is helpful, but not always.
