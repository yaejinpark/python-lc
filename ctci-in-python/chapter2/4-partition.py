from LinkedList import *
# All nodes greater than the partition comes after nodes lesser than partition.

# Method 1: Have two separate linked list and then merge them
def partition1(LL,partition):
    # LL1 = before partition value, LL2 = after partition value
    LL1start, LL1end = None, None
    LL2start, LL2end = None, None

    LL1 = linkedList()
    LL2 = linkedList()

    currentNode = LL.head = LL.head.next

    while currentNode != None:
        nextNode = currentNode.next
        currentNode.next = None

        # If node data is smaller than the partition value, insert current node into LL1's end
        if currentNode.data < partition:
            if LL1start == None:
                LL1start, LL1end = currentNode, currentNode
                LL1.append(currentNode.data)
            else:
                LL1end.next, LL1end = currentNode, currentNode
                LL1.append(currentNode.data)
        else:
            if LL2start == None:
                LL2start, LL2end = currentNode, currentNode
                LL2.append(currentNode.data)
            else:
                LL2end.next, LL2end = currentNode, currentNode
                LL2.append(currentNode.data)

        currentNode = nextNode

    # If LL smaller than partition value is empty, return the other nodes
    if LL1start == None:
        return LL2.head

    # Merging the two LL's
    LL1end.next = LL2start

    # Just for printing purpose
    LL1.seeAllNodes()
    LL2.seeAllNodes()

    return(LL1.head)

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(4)
testLL1.append(1)
testLL1.append(5)
testLL1.append(6)
testLL1.append(7)
partition1(testLL1,3)

print("\nNext test case:\n")

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
partition1(testLL2,5)
