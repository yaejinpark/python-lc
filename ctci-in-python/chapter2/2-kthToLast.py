#Find the kth to last element of a linked list

from LinkedList import *

#Solution 1: Simple - just iterate through the linked list
def kthNode(LL,k):

    #Head node also counts as a node, so default length is 1
    LLlength = 1
    currentNode = LL.head
    while currentNode.next != None:
        LLlength += 1
        currentNode = currentNode.next

    #If requested k is bigger than the linked list, it won't work.
    if k > LLlength:
        print("k is bigger than the length of the linked list")
        return LL.head

    currentNode = LL.head
    for n in range(LLlength+1):
        if n == LLlength-k:
            print(currentNode.data)
            return LL.head
        currentNode = currentNode.next

#TL;DR
#Depending on what I set the LL's length's default value to (0 or 1), I may have to add 1 to line 22
#LLlength - k + 1 if I started LLlength as 0

#Solution 2: Using two pointers
def kthNode2(LL,k):
    pointer1 = LL.head
    pointer2 = LL.head

    # Move pointer1 ahead of pointer2 by k
    for n in range(0, k):
        if pointer1 == None:
            return LL.head
        pointer1 = pointer1.next

    #Iterate through the remaining elements for pointer1
    #When pointer1 hits the end of the Linked List, pointer2 should be at kth from last.
    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    print("kth to last element is:", pointer2.data)

#TL;DR
#Solution 2 is useful because it doesn't iterate through the whole Linked List.
# 1. Have one pointer start at the kth element from last
# 2. Then move both pointers (the other pointer starts at beginning) until first pointer hits the end
#When the length of the Linked List is unknown, this is the best way to go.

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(4)
testLL1.append(1)
testLL1.append(5)
testLL1.append(6)
testLL1.append(7)
# kthNode(testLL1,5) #Should print 4
kthNode2(testLL1,5)

testLL2 = linkedList()
testLL2.append(2)
testLL2.append(7)
testLL2.append(8)
testLL2.append(1)
testLL2.append(1)
testLL2.append(5)
testLL2.append(6)
testLL2.append(7)
testLL2.append(9)
# kthNode(testLL2,3) #Should print 6

testLL3 = linkedList()
testLL3.append(1)
# kthNode(testLL3,3) #Should not be successful