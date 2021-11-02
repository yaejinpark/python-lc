from LinkedList import *

# If there is a loop, return the node at the beginning of the loop
def loopDetection(LL):
    fast = slow = LL.head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break

    if fast == None or fast.next == None:
        return None

    slow = LL.head

    while fast != slow and fast.next != None:
        fast = fast.next
        slow = slow.next

    return fast

# TL; DR
# Think of two race cars going at a different speed in the same track. There will be a collision.
# 1. Have a slow pointer and a faster pointer go at 1 node, 2 node pace respectively.
# 2. When there's a collision, move back slow pointer to the LL's head.
# 3. Move both pointers at the same pace (one node at a time). Return the

testLL1 = linkedList()
testLL1.append(1)
testLL1.append(2)
testLL1.append(3)
testLL1.append(4)
testLL1.append(5)
testLL1.append(6)
testLL1.append(7)
testLL1.append(5)
loopDetection(testLL1) # There is a loop

testLL2 = linkedList()
testLL2.append(2)
testLL2.append(7)
testLL2.append(8)
testLL2.append(3)
testLL2.append(4)
testLL2.append(5)
testLL2.append(6)
testLL2.append(1)
testLL2.append(9)
loopDetection(testLL2) # No loop