#This is a separate note for reviewing Linked Lists
#Also a good review for Python constructors

class node:
    def __init__(self, data = 0):
        #By default, a node has a value and no trailing nodes
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        # We access a LL first through the head node
        self.head = node()

    # Methods for manipulating LL
    def append(self, data):
        newTail = node(data)

        # Iteration always starts from the head node
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next

        # Append new tail node at the end of the iteration
        currentNode.next = newTail

    # Append a new node at the head of the LL
    def appendToHead(self, data):
        newNode = node(data)

        newNode.next = self.head
        self.head = newNode

        return self.head

    def delete(self, headNode, targetValue):
        currentNode = headNode

        #If the head node is the deletion target value, delete the head and return None
        if headNode == targetValue:
            return headNode.next

        #Iterate through the LL, if next node is the deletion target, "remove" that target
        while currentNode.next != None:
            if currentNode.next == targetValue:
                currentNode.next = currentNode.next.next
                #Head doesn't change.
                return headNode

            currentNode = currentNode.next
        return headNode

    #If you just print the LL, you'll get the memory address instead of the elements.
    #Method for displaying all values within the LL as a list

    def seeAllNodes(self):
        currentNode = self.head
        nodes = []

        while currentNode.next != None:
            currentNode = currentNode.next
            nodes.append(currentNode.data)

        print(nodes)

    def getLength(self):
        currentNode = self.head
        counter = 0

        if self.head == None:
            return 0

        while currentNode.next != None:
            counter += 1
            currentNode = currentNode.next
        return counter

        print(nodes)

    def getTail(self):
        currentNode = self.head

        while currentNode.next != None:
            currentNode = currentNode.next

        return currentNode