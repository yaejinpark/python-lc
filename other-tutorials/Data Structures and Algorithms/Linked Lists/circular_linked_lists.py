# Import Nodes class
from nodes import Node

# A CLL is great for modeling continuous looping objects such as a Monopoly board or a race track.

# Very similar to the regular linked lists except: 
# 1. New nodes will be inserted right after the root node
# 2. The end node will point to the root node

class CircularLinkedList:
	def __init__(self,root=None):
		self.root = root
		self.size = 0

	def add(self,data):
		if self.root == None:
			self.root = Node(data)
			self.root.next_node = self.root # Remember this line since the LL is circular!
		else:
			# Long way of doing add when root node exists
			# dummy = self.root.next_node
			# self.root.next_node = new_node
			# new_node.next_node = dummy

			# More efficient way:
			new_node = Node(data, self.root.next_node)
			self.root.next_node = new_node
		self.size += 1

	def find(self, target_data):
		this_node = self.root
		while True:
			if this_node.data == target_data:
				return target_data
			elif this_node.next_node == self.root: # This condition would be true if we circled the whole loop once
				return False 
			
			this_node = this_node.next_node

	def remove(self, target_data):
		this_node = self.root
		prev_node = None

		while True:
			if this_node.data == target_data: # If the the node is found...
				if prev_node is not None: # If the target data is not the root node...
					prev_node.next_node = this_node.next_node
				else:
					while this_node.next_node != self.root: # If the root needs to be deleted...
						this_node = this_node.next_node # Find the very last node
					this_node.next_node = self.root.next_node
					self.root = self.root.next_node # Change the root
				self.size -= -1
				return True # Data removed

			elif this_node.next_node == self.root: # If there is only the root node and it doesn't match the target...
				return False
			prev_node = this_node
			this_node = this_node.next_node

	def print_list(self):
		if self.root is None:
			return

		this_node = self.root

		print(this_node, end="->")
		while this_node.next_node != self.root:
			this_node = this_node.next_node
			print(this_node, end='->')
		print()


cll = CircularLinkedList()
for i in [5,7,3,8,9]:
	cll.add(i)

print("size="+str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root

print(my_node, end='->')
for i in range(8): # Range is bigger than the number of unique nodes to prove it is indeed circular
	my_node = my_node.next_node
	print(my_node, end='->')
print()

cll.print_list() # Print a complete loop of the cll
cll.remove(8)
cll.print_list()