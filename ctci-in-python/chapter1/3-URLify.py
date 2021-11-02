#Change all spaces in a string into %20

def urlify(input):
    print(input.strip().replace(" ","%20"))


testInput = "Mr John Smith     "
testInput2 = "Orange Fat     Tabbies"

urlify(testInput)
urlify(testInput2)

#TL;DR
#strip() is for getting rid of blank spaces in the ends of a string
#replace() is more useful for blank spaces between characters
#Try to get rid of the extra %20's in testInput2