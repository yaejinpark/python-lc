#Remove duplicate nodes from the LL
#Follow up: Don't use temporary buffer

from LinkedList import *

def removeDup(LL):
    #Create a dictionary to use as a buffer for records
    isUniqueNode = {}
    currentNode = LL.head

    #If head node is the only node, no duplicates to count
    if currentNode.next == None:
        return LL.head

    #If node is duplicate, "delete" or just move the pointer to the next node
    while currentNode.next != None:
        if currentNode.next.data in isUniqueNode:
            isUniqueNode[currentNode.next.data] = False
            currentNode.next = currentNode.next.next
        else:
            isUniqueNode[currentNode.next.data] = True
            currentNode = currentNode.next

    #Display the final results
    LL.seeAllNodes()

    #return the head node
    return LL.head

#Don't use dictionaries but producte the same results as removeDup()
def followUp(LL):
    currentNode = LL.head

    if LL.head == None:
        return LL.head

    while currentNode != None:
        #Start a runner pointer and the current node pointer at the same spot
        runnerNode = currentNode
        #Have the runner pointer move ahead of the current node to find the duplicate values
        while runnerNode.next != None:
            #If the runner pointer finds the same value as the current node pointer, delete the duplicate
            if runnerNode.next.data == currentNode.data:
                runnerNode.next = runnerNode.next.next
            #Otherwise, let the runner pointer iterate through the remaining nodes
            else:
                runnerNode = runnerNode.next
                #Move current node pointer to the next node
        currentNode = currentNode.next

    LL.seeAllNodes()
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
# removeDup(testLL1)
followUp(testLL1)

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
# removeDup(testLL2)
followUp(testLL2)

#TL;DR:
#I need to consider a corner case where the last node is a duplicate
#The first method using a dictionary takes O(N) time with O(N) space
#The second method (no buffer) takes O(N^2) time with O(1) space
#In Pycharm, importing another py module doesn't work unless I mark the folder as source root.
#The error I was stuck on for 20 min: runnerNode.next.data == currentNode.data
#Even if a node has the same data(value) as another node, those two nodes are not equal.
