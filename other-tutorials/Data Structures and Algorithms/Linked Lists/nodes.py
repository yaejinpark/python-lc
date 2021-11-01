# Every node has two parts: data/val and a pointer to the next node.
# A bi-directional LL will have a pointer for the "previous" node, but ignore that for regular LL.

class Node:
	def __init__(self,data, n=None, p=None):
		self.data = data
		self.next_node = n
		self.prev_node = p

	def __str__(self):
		return ( '(' + str(self.data) + ')')