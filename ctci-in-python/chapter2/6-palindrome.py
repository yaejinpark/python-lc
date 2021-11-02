from LinkedList import *
from math import ceil

def palindrome (LL):
    LLlength = LL.getLength()
    pivotPoint = ceil(LLlength/2)

    currentNode = LL.head
    runnerNode = currentNode

    # Have another pointer iterate up to the pivot point
    for i in range (pivotPoint):
        runnerNode = runnerNode.next

    beforePivot, afterPivot = [], []

    # Store the first half of the LL into the beforePivot list
    while currentNode.next != runnerNode.next:
        beforePivot.append(currentNode.next.data)
        currentNode = currentNode.next

    # Store the second half of the LL into the afterPivot list
    while runnerNode != None:
        afterPivot.append(runnerNode.data)
        runnerNode = runnerNode.next

    # If the first half matches the reverse of the second half of the LL, then it's a palindrome.
    LL.seeAllNodes()

    if beforePivot == afterPivot[::-1]:
        print("This is a palindrome")
        return True
    else:
        print("This is not a palindrome")
        return False

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(4)
testLL1.append(3)
testLL1.append(2)
testLL1.append(1)
palindrome(testLL1) # Should be a palindrome

print("\nNext test case:\n")

testLL2 = linkedList()
testLL2.append(2)
testLL2.append(7)
testLL2.append(8)
testLL2.append(1)
testLL2.append(3)
testLL2.append(5)
testLL2.append(6)
testLL2.append(7)
testLL2.append(9)
testLL2.append(9)

palindrome(testLL2)

# TL;DR
# Having multiple pointers makes life easier.
# Similar to the runner up pointer problem somewhere in this chapter.
# This is NOT asking for a palindrome permutation, so it's not looking for a potential to be a palindrome.
# It HAS to be a palindrome.