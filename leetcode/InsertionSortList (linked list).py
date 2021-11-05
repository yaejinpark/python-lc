# Problem Link: https://leetcode.com/problems/insertion-sort-list/

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
	if head is None or head.next_node is None: # In case the list is empty or has a single node
		return head

	dummy = Node(None) # Acts as the head of the new, sorted linked list
	current = head # For iterating over each node in the given, unsorted linked list

	while current:
		# Whichever value that is being added to the new linked list will be between these two:
		prev_pointer = dummy
		next_pointer = dummy.next_node

		while next_pointer:
			if current.data < next_pointer.data: # Break out of the while loop if there is a value to insert between prev and next
				break
			prev_pointer = prev_pointer.next_node # Move each of the pointers by 1
			next_pointer = next_pointer.next_node

		# If current is smaller than next_pointer.data...
		temp = current.next_node

		current.next_node = next_pointer
		prev_pointer.next_node = current

		current = temp # Can't do the usual current = current.next because current.next = next_pointer. So use temp.

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