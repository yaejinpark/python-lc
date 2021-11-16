# Searching elements is fast because every time I'm looking for an element, I'm halving the search base (right and left)
# That's why the search complexity is O(log n)

# Two ways of traversing in a BST - Breadth First Search (BFS) and Depth First Search (DFS).

# Always visit left subtree first!

# BFS

# DFS
# In order traversal
# Pre order traversal - If root node is visited before subtrees, then it is pre order.
# Post order traversal

class BST:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self,data):
		if data == self.data: # Case 1: Data I'm trying to add already exists
			return 

		if data < self.data: # Case 2: Data I'm trying to add is less than the current node
			# add data in left subtree after checking we are at a leaf node
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BST(data)

		else: # Case 3: Data I'm trying to add is greater than the current node
			# add data in right subtree
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BST(data)

	# In order traversals are used for giving nodes an ascending order. 

	def in_order_traversal(self): # Return a list of elements in the BST after in order traversal
		elements = []

		# Visit left subtree first
		if self.left:
			elements += self.left.in_order_traversal()

		# Visit root (base) node
		elements.append(self.data)

		# Visit right subtree
		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	# Pre order traversals are used to create a copy of the tree or to get its prefix expression.
	# A prefix notation is useful to make long expressions less repetitive. 
	# https://clojurebridgelondon.github.io/workshop/simple-values/prefix-notation.html

	def pre_order_traversal(self): # Return a list of elements in the BST after pre order traversal
		elements = []

		# Visit the root node
		elements.append(self.data)
		root = self

		# Visit and traverse the left subtree
		if self.left:
			elements += self.left.pre_order_traversal()

		# Visit and traverse the right subtree
		if self.right:
			elements += self.right.pre_order_traversal()

		return elements

	# Post order traversals are useful when deleting the tree because children nodes must be deleted before their parents.

	def post_order_traversal(self): # Return a list of elements in the BST after post order traversal
		elements = []

		root = self.data

		# Visit and traverse the left subtree
		if self.left:
			elements += self.left.post_order_traversal()

		# Visit and traverse the right subtree
		if self.right:
			elements += self.right.post_order_traversal()

		# Visit the root node
		elements.append(root)

		return elements

	def search(self,target_data): # Search for a specific value in the tree
		if self.data == target_data:
			return True

		if target_data < self.data: # Target data MIGHT be in the left subtree
			if self.left:
				return self.left.search(target_data)
			else:
				return False

		if target_data > self.data: # Target data MIGHT be in the right subtree
			if self.right:
				return self.right.search(target_data)
			else:
				return False

	def find_min(self): # Find the minimum value in a BST
		if self.data is None: # If the tree is empty, return None
			return None

		if self.left is None: # If there is a left child node, keep traversing left until you reach a node that doesn't. Then return data
			return self.data
		return self.left.find_min()

	def find_max(self): # Find the maximum value in a BST
		if self.data is None: # If the treey is empty, return None
			return None

		if self.right is None: # If there is a right child node, keep traversing right until you reach a node that doesn't. Then return data.
			return self.data
		return self.right.find_max()

	def delete(self,target_data): # Delete a specific node in the tree
	# Case 1: Delete a node with no child
	# Case 2: Delete a node with one child
	# Case 3: Delete a node with two children - most tricky

	# Copy the minimum from the target's right subtree to the target node's spot
	# ...Or copy the maximum from the target's left subtree

		if target_data < self.data:
			if self.left:
				self.left = self.left.delete(target_data)
		elif target_data > self.data:
			if self.right:
				self.right.delete(target_data)
		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				return self.right 
			if self.right is None:
				return self.right

			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.delete(min_val) # Returns the new right subtree

		return self

def build_tree(elements):
	root = BST(elements[0]) # Assign first element as root node

	for i in range(1,len(elements)):
		root.add_child(elements[i])

	return root

my_tree = build_tree([17,4,1,20,9,23,18,34])
print(my_tree.in_order_traversal()) # This will sort the input list. Great for implementing set without using set()
print(my_tree.search(23))
print(my_tree.search(21))
print(my_tree.find_min())
print(my_tree.find_max())
print(my_tree.pre_order_traversal())
print(my_tree.post_order_traversal())
my_tree.delete(20)
print(my_tree.in_order_traversal())
