# In a binary search tree, each node is greater than every node in its left subtree (trees beneath the root node)
# Each node is less than every node than its right subtree.
# Most functions related to tree operations are recursive.

# Advantages:
# 1. Easy to implement because trees use recursion for most operations
# 2. Speed. Insert, Delete, Find in O(height) = O(log n)

# Basic Tree Operations:
# Insert - start at root, always insert as a leaf
# Find - find a specific node.
# Delete - delete a certain node and promote children, if necessary.
# Get Size - find the number of nodes in a tree. Works recursively.
# Traversals - Preorder traversal and inorder traversal are some of the common techniques

class Tree:
	def __init__(self,data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def insert(self, data):
		if self.data == data: # Don't add duplicate value
			return False
		elif self.data > data: # Case 1: new data is smaller than the existing node's data
			if self.left is not None: 
				return self.left.insert(data)
			else:
				self.left = Tree(data)
				return True
		else: # Case 2: new data is bigger than the existing node's data
			if self.right is not None:
				return self.right.insert(data)
			else:
				self.right = Tree(data)

	#def find(self, target_data):
