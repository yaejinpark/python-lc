# Importing LinkedList class file in other directory
import sys
sys.path.append('../other-tutorials/Data Structures and Algorithms/Linked Lists')
from regular_linked_lists import LinkedList

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

	if head is None or head.next_node is None:
		return head

	current = head
	key = current.next_node

	while current.data > key.data and key.next_node:
		current,key = key,current
		key = key.next_node

	while head is not None: # Printing to see final results
		print(head)
		head = head.next_node	

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

sorted_ll = insertion_sort_list(test_ll1)
print(sorted_ll)