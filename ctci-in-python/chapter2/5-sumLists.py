from LinkedList import *

def sumLists(LL1,LL2):
    resultLL = linkedList()

    # Current node pointers for both LL's
    cn1, cn2 = LL1.head, LL2.head
    carry = 0

    while cn1.next != None or cn2.next != None:
        sumOfNodes = carry

        # Add LL1's current node's value to the sum variable
        if cn1 != None:
            sumOfNodes += cn1.next.data
            cn1 = cn1.next

        # Add LL2's current node's value to the sum variable
        if cn2 != None:
            sumOfNodes += cn2.next.data
            cn2 = cn2.next

        # Carry is not incremented, and sumOfNodes starts with carry's value (0) each loop.
        carry = sumOfNodes // 10 # Gives me the floor integer value of a division

        # Modulo 10 gives me the remainder after dividing the sum by 10
        resultLL.append(sumOfNodes % 10)

    resultLL.seeAllNodes()
    return resultLL.head

def followup(LL1, LL2):
    LL1length = LL1.getLength()
    LL2length = LL2.getLength()

    # Must consider the difference in the length of both linked lists
    # Shorter lists gets padded with 0's at its head node
    if LL1length < LL2length:
       for zeros in range(LL2length - LL1length):
           LL1.appendToHead(0)
    else:
        for zeros in range (LL1length - LL2length):
            LL2.appendToHead(0)

    cn1, cn2 = LL1.head, LL2.head

    sumOfNodes = 0

    while cn1.next != None and cn2.next != None:
        # This is the key to the calculation without using unnecessary carry variables
        sumOfNodes = sumOfNodes * 10 + cn1.next.data + cn2.next.data
        cn1 = cn1.next
        cn2 = cn2.next

    # Store the sum result in a dummy list
    dummyList = [int(i) for i in str(sumOfNodes)]

    # Append the numbers in the dummy list to the linked list
    resultLL = linkedList()
    for nums in dummyList:
        resultLL.append(nums)

    resultLL.seeAllNodes()
    return resultLL.head

# First Linked List
testLL1 = linkedList()
testLL1.append(7)
testLL1.append(1)
testLL1.append(6)

# Second Linked List
testLL2 = linkedList()
testLL2.append(5)
testLL2.append(9)
testLL2.append(2)

# sumLists(testLL1, testLL2)

# For Followup
testLL3 = linkedList()
testLL3.append(6)
testLL3.append(1)
testLL3.append(7)

testLL4 = linkedList()
testLL4.append(2)
testLL4.append(9)
testLL4.append(5)

followup(testLL3, testLL4)

# TL;DR
# When it comes to dealing with multiple linked lists, expect to use more than one pointer
# I first tried summing the values by converting the LLs to lists and the lists back to LL...this is stupid.
# carry never exceeds 1 because I don't increment it manually anywhere, and so resets back to 0 on its own.