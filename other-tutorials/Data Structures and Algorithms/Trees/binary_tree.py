# NOTE: BST is a special case of binary tree where the nodes have a certain order.

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
		if self.data == data: # Case 1: new data is the same as one of the existing nodes - Don't add duplicate value
			return False
		elif self.data > data: # Case 2: new data is smaller than the existing node's data
			if self.left is not None: 
				return self.left.insert(data) # descend down the left subtree recursively
			else:
				self.left = Tree(data) # set new data as new left subtree
				return True
		else: # Case 3: new data is bigger than the existing node's data
			if self.right is not None:
				return self.right.insert(data) # descend down the right subtree recursively
			else:
				self.right = Tree(data) # set new data as new right subtree

	def find(self, data):
		if self.data == data: # Case 1: data is found right away, return it
			return data
		elif self.data > data: # Case 2: target data is smaller than the current data
			if self.left is None:
				return False
			else:
				return self.left.find(data) # Recursively look for target data on the left subtree
		elif self.data < data: # Case 3: target data is bigger than the current data
			if self.data.right is None:
				return False
			else:
				return self.right.find(data) # Recursively look for target data on the right subtree

	def get_size(self):
		if self.left is not None and self.right is not None:
			return 1 + self.left.get_size() + self.right.get_size()
		elif self.left:
			return 1 + self.left.get_size()
		elif self.right:
			return 1 + self.right.get_size()
		else:
			return 1

	def preorder(self):
		if self is not None:
			print(self.data, end=' ')
			if self.left is not None:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def inorder(self):
		if self is not None:
			if self.left is not None:
				self.left.inorder()
			print(self.data, end=' ')
			if self.right is not None:
				self.right.inorder()