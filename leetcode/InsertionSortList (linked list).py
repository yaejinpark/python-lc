# Importing LinkedList class file in other directory
import sys
sys.path.append('../other-tutorials/Data Structures and Algorithms/Linked Lists')
from regular_linked_lists import LinkedList
from nodes import Node

# class Node:
# 	def __init__(self,data, n=None, p=None):
# 		self.data = data
# 		self.next_node = n
# 		self.prev_node = p

# class LinkedList:
# 	def __init__(self,root=None):
# 		self.root = root
# 		self.size = 0

def insertion_sort_list(ll):
	head = ll.root
	new_list = LinkedList()

	if head is None or head.next_node is None: # In case the list is empty or has a single node
		return head

	dummy = Node(None)
	current = head

	while current:
		prev = dummy

		while prev.next_node and prev.next_node.data < current.data:
			prev = prev.next_node

		next_node = current.next_node

		current.next_node = prev.next_node
		prev.next_node = current

		current = next_node

	while dummy.next_node is not None: # Printing to see final results
		print(dummy.next_node)
		dummy = dummy.next_node
	return dummy.next_node

test_ll1 = LinkedList()
test_ll1.add_back(4)
test_ll1.add_back(2)
test_ll1.add_back(1)
test_ll1.add_back(3)

test_ll2 = LinkedList()
test_ll2.add_back(-1)
test_ll2.add_back(5)
test_ll2.add_back(3)
test_ll2.add_back(4)
test_ll2.add_back(0)

test_ll3 = LinkedList()

sorted_ll = insertion_sort_list(test_ll1)
print(sorted_ll)

# Working Solution back up

# def insertion_sort_list(ll):
# 	head = ll.root
# 	new_list = LinkedList()

# 	if head is None or head.next_node is None: # In case the list is empty or has a single node
# 		return head

# 	dummy = Node(0)
# 	current = head

# 	while current:
# 		prev = dummy

# 		while prev.next_node and prev.next_node.data < current.data:
# 			prev = prev.next_node

# 		next_node = current.next_node

# 		current.next_node = prev.next_node
# 		prev.next_node = current

# 		current = next_node

# 	while dummy.next_node is not None: # Printing to see final results
# 		print(dummy.next_node)
# 		dummy = dummy.next_node
# 	return dummy.next_node