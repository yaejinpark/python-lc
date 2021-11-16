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

	def in_order_traversal(self): # Return a list of elements in the BST in a specific order
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

	# Exercises
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
