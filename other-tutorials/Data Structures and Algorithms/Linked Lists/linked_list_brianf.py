#Following tutorials from
#Brian Faure on YouTube

class node:
    def __init__ (self, data = None):
        self.data = data
        #by default is none for now, but can be overwritten later
        self.next = None

class linked_list:
    def __init__ (self):
        #creating a head node
        self.head = node()

    def append(self, data):
        #Create a new node
        newNode = node(data)
        #Starting at the head node, so current is head by default
        currentNode = self.head

        while currentNode.next != None:
            #If there is a next node, move onto it
            currentNode = currentNode.next

        #After iterating through all nodes, add the new node
        currentNode.next = newNode

    #How large is this data structure?
    def length(self):
        currentNode = self.head
        totalNodes = 0
        while currentNode.next != None:
            totalNodes += 1
            currentNode = currentNode.next
        #Done counting number of nodes!
        return totalNodes

    def display(self):
        elems = []
        currentNode = self.head

        #Iterate through all nodes and store their data in an array
        while currentNode.next != None:
            currentNode = currentNode.next
            elems.append(currentNode.data)
        #Print the arrays
        print(elems)

    def getNode(self,index):
        #Check index is not out of range
        if index >= self.length:
            print("Index is out of range. Check again.")
            return None

        #Again, start at the head node
        currentIndex = 0
        currentNode = self.head

        #Iterate through all nodes, then print the one that matches the given index
        while True:
            currentNode = currentNode.next
            if currentIndex == index:
                return currentNode.data
            currentIndex += 1

    def eraseNode(self,index):
        if index >= self.length:
            print("Index is out of range. Check again.")
            return None

        currentIndex = 0
        currentNode = self.head

        while True:
            #After deleting a node, the pointer should point at the node next to the deleted.
            previousNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                previousNode.next = currentNode.next
                return
            currentIndex += 1

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

#Erase 1
my_list.eraseNode(0)

my_list.display()

print(my_list.getNode(1))
