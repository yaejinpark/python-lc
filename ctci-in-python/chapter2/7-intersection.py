from LinkedList import *

def isIntersecting(LL1, LL2):
    # Big Hint: Once the nodes intersect, the trailing nodes are the same for the two linked lists
    # No need to use a Hash Table
    if LL1.getTail().data != LL2.getTail().data:
        print("LLs have different tail nodes.")
        return False

    # Padding shorter LL with zeros with two LL's have different lengths
    LL1length, LL2length = LL1.getLength(), LL2.getLength()

    if LL1length < LL2length:
        for zeros in range(LL2length - LL1length):
            LL1.appendToHead(0)
    else:
        for zeros in range(LL1length - LL2length):
            LL2.appendToHead(0)

    cn1, cn2 = LL1.head, LL2.head

    while cn1.data != cn2.data:
        cn1 = cn1.next
        cn2 = cn2.next

    print("There is an intersection")
    return LL1.head

# Another attempt without padding zeros to the head of the LL
def isIntersecting2 (LL1, LL2):

    if LL1.getTail().data != LL2.getTail().data:
        print("LLs have different tail nodes.")
        return False

    # Determine which is the shorter or longer LL
    shorter = LL1 if LL1.getLength() < LL2.getLength() else LL2
    longer = LL1 if LL1.getLength() > LL2.getLength() else LL2

    lengthDiff = longer.getLength() - shorter.getLength()

    longCN = longer.head
    shortCN = shorter.head

    # Iterate through longer LL for the duration of the difference of the length
    for nodes in range(lengthDiff):
        longCN = longCN.next

    # If no intersection is found, move on to next node for both LL's
    while longCN != shortCN:
        longCN = longCN.next
        shortCN = shortCN.next

    print("There is an intersection")

    # I can return shorter LL if I want to. Any LL works
    return longer.head

# TL;DR
# Intersecting LL's should have the same tail.
# Instead of padding zeros, just iterate through the longer LL a bit until it matches the length of the shorter LL

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(1)
testLL1.append(1)
testLL1.append(1)
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(3)

testLL2 = linkedList()
testLL2.append(7)
testLL2.append(7)
testLL2.append(7)
testLL2.append(2)
testLL2.append(3)
testLL2.append(3)

testLL3 = linkedList()
testLL3.append(5)
testLL3.append(5)
testLL3.append(5)

testLL4 = linkedList()
testLL4.append(4)
testLL4.append(4)
testLL4.append(4)
testLL4.append(5)

print("First Test Case\n")
isIntersecting2(testLL1, testLL2)
print("\nSecond Test Case\n")
isIntersecting2(testLL1, testLL3)
print("\nThird Test Case\n")
isIntersecting2(testLL3, testLL4)