#Tutorial from Brian Faure's YouTube Channel
#Note: A tree is binary if there are two connections leaving each node

from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        #left child is smaller than the current value
        self.leftChild = None
        #right child is bigger than the current value
        self.rightChild = None

#A wrapper that handles the node class
#User interacts only with this class
class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        #Recursive case of inserting
        else:
            self._insert(value, self.root)

    def _insert(self,value,currentNode):
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value)
            else:
                self._insert(value, currentNode.leftChild)
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert(value, currentNode.rightChild)
        else:
            print("Duplicate value nodes not counted in this tree.")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, currentNode):
        if currentNode != None:
            self._printTree(currentNode.leftChild)
            print("Current node value is:", str(currentNode.value))
            self._printTree(currentNode.rightChild)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        #Tree has height of 0 if root is None
        else:
            return 0

    def _height(self, currentNode, currentHeight):
        if currentNode == None:
            return currentHeight
        leftHeight = self._height(currentNode.leftChild,currentHeight+1)
        rightHeight = self._height(currentNode.rightChild,currentHeight+1)

        return max(leftHeight, rightHeight)

    #Look for a specific value in a tree
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, currentNode):
        if value == currentNode.value:
            return True
        #If the value I'm looking for is smaller than the current node and there are still left child nodes,
        #Do recursion of search
        #Same applies for when value is bigger than the current node and right child exists
        elif value < currentNode.value and currentNode.leftChild != None:
            return self._search(value,currentNode.leftChild)
        elif value > currentNode.value and currentNode.rightChild != None:
            return self._search(value,currentNode.rightChild)
        #Still can't find the node, return false
        return False

#For creating some random data and filling a tree
def fillTree(tree, elem=100, maxInt=1000):
    for _ in range(elem):
        currentElement = randint(0,maxInt)
        tree.insert(currentElement)
    return tree

newBST = Bst()
# newBST = fillTree(newBST)
newBST.insert(0)
newBST.insert(1)
newBST.insert(2)
newBST.insert(3)
newBST.insert(4)
newBST.insert(5)
newBST.insert(6)
newBST.insert(7)
newBST.printTree()
print("The tree's height is:", newBST.height())
print("Does the value exist in the tree?",newBST.search(5))

