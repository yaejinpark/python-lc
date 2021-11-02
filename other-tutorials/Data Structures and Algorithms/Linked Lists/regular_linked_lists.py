# Import Nodes class
from nodes import Node

# Starting node is known as the root node.

# Attributes: 
# Root - pointer to the beginning of the LL
# Size - number of nodes in LL

# Operations:
# find(data), add(data), remove(data), print_list()

class LinkedList:
	def __init__(self,root=None):
		self.root = root
		self.size = 0

	# Add a new node in front of the root node
	def add_front(self,data):
		new_node = Node(data,self.root)
		self.root = new_node
		self.size += 1

	# Add a new node on the tail
	def add_back(self,data):
		new_node = Node(data)
		this_node = self.root

		if self.root == None:
			self.root = new_node
		else:
			while this_node.next_node is not None:
				this_node = this_node.next_node
			this_node.next_node = new_node
		self.size += 1

	# Iterate through all of the nodes in the LL to find the target data
	def find(self,target_data):
		this_node = self.root

		while this_node is not None:
			if this_node.data == target_data:
				return target_data
			else:
				this_node = this.node.next_node

		return None

	def remove(self, target_data):
		this_node = self.root
		prev_node = None

		while this_node is not None:
			if this_node.data == target_data:
				if prev_node is not None: # If the target node is not a root node...
					prev_node.next_node = this_node.next_node
				else: # Else if the target node is the root node...
					self.root = this_node.next_node
				self.size -= 1
				return True # Data removed, return true

			else:
				prev_node = this_node
				this_node = this_node.next_node
		return False # Data not found!

	def print_list(self):
		this_node = self.root

		while this_node is not None:
			print(this_node, end='->')
			this_node = this_node.next_node
		print('None')

# my_LL = LinkedList()
# my_LL.add_front(5)
# my_LL.add_front(6)
# my_LL.add_back(7)
# my_LL.remove(5)

# my_LL.print_list()
# print(my_LL.size)


