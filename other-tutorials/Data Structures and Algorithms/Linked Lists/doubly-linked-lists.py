# Import Nodes class
from nodes import Node

# Advantages:
# 1. Can iterate the LL in either direction
# 2. Can delete a node without iterating through the list (if given a pointer to the node)

class DoublyLinkedList:
	def __init__(self,root=None):
		self.root = root
		self.last = root
		self.size = 0

	def add_back(self,data): # Add node to the tail end of the LL
		if self.size == 0:
			self.root = Node(data)
			self.last = self.root
		else:
			new_node = Node(data,None,self.last)
			self.last.next_node = new_node # First, set the next node of the current last to new node
			self.last = new_node # Then, move the pointer of the last node to point the new node
		self.size += 1

	def add_front(self,data): # Add node in front of the root node
		if self.size == 0:
			self.root = Node(data)
			self.last = self.root
		else:
			new_node = Node(data,self.root)
			self.root.prev_node = new_node # First, set the previous node of the root node to the new node
			self.root = new_node # Then, have the root pointer point to the new node
		self.size += 1

	def find(self,target_data):
		this_node = self.root

		while this_node is not None: # Iterating through the DLL
			if this_node.data == target_data: # Node with target value found
				return target_data
			elif this_node.next_node == None: # Node with target value not found
				return False
			else:
				this_node = this_node.next_node

	def remove(self,target_data):
		this_node = self.root

		while this_node is not None:
			if this_node.data == target_data:
				# Case 1: Deleting a node in the middle of the DLL - not in the root or the tail end
				if this_node.prev_node is not None:
					if this_node.next_node is not None:
						this_node.prev_node.next_node = this_node.next_node # Previous node points to current node's next node
						this_node.next_node.prev_node = this_node.prev_node # Next node points to current node's previous node
					# Case 2: Delete the last node
					else:
						this_node.prev_node.next_node = None # Previous node's next now points to None
						self.last = this_node.prev_node # The last node is the previous node now
				# Case 3: Delete the root node
				else:
					self.root = this_node.next_node # Root now points to the root's next node
					this_node.next_node.prev_node = self.root # The next node is now the root
				self.size -= 1
				return True 
			else:
				this_node = this_node.next_node

	def print_list(self):
		if self.root is None:
			return
		
		this_node = self.root
		print(this_node,end='->')
		while this_node.next_node is not None:
			this_node = this_node.next_node
			print(this_node,end='->')
		print()

my_dll = DoublyLinkedList()
my_dll2 = DoublyLinkedList()
test_vals = [1,4,3,8,5,4]
for i in test_vals:
	my_dll.add_front(i)
print("my_dll's size is: ",my_dll.size)
my_dll.print_list()

for i in test_vals:
	my_dll2.add_back(i)
print("my_dll2's size is: ",my_dll2.size)
my_dll2.print_list()

print(my_dll2.find(8))

my_dll2.remove(8)
my_dll2.print_list()
