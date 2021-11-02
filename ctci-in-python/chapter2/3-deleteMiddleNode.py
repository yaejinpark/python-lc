from LinkedList import *

#Middle doesn't necessarily mean smack in the middle (len/2).
#Depending on the interviewer, it will probably mean any node but the first or the last.

def deleteMid(LL, targetNode):
    currentNode = LL.head
    print("Linked list before deletion: ")
    LL.seeAllNodes()
    while currentNode.next != None:
        if currentNode.next.data == targetNode:
            currentNode.next = currentNode.next.next
        currentNode = currentNode.next
    print("Linked list after deletion: ")
    LL.seeAllNodes()
    print("\n")
    return LL.head

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(4)
testLL1.append(1)
testLL1.append(5)
testLL1.append(6)
testLL1.append(7)
deleteMid(testLL1,3)

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
deleteMid(testLL2,8)
