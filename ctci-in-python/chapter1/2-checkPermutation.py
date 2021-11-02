#abcd is a permutation of acefdghb
#All characters of a shorter string will be a part of the longer string.
#First, go with sorting alphabetically

def checkPerm(shortString, longString):
    sortedShort = ''.join(sorted(shortString))
    for char in sortedShort:
        if char not in longString:
            return False
    return True

testShort1 = 'abcd'
testLong1 = 'acefdghb'
testShort2 = 'aacbd'
testLong2 = 'abawejfakwjenfawkejfwaejfalwefawegeewgaerfgfcd'

print(checkPerm(testShort1,testLong1))
print(checkPerm(testShort2,testLong2))

#TL;DR
#Unless I'm dealing with a really, really long string, sorted() shouldn't cause too much damage
#If I want to sort a string and store it in a variable, do ''.join(sorted(string))
#Try to come up with a more efficient solution when I get a chance