# A MaxHeap is a complete binary tree.
# Every node is less than or equal to its parent.
# It's structured this way so that we can remove the max number of the heap anytime we want to.

# Insert in O(log n)
# Get Max in O(1)
# Remove Max in O(log n)

# Push (insert) - "Float or Bubble" up the value to its position
# Peek (get max) - Return the value at the top of the heap, index 0
# Pop (remove max) - move max to end of array, delete, and bubble down the item at index 0 to its proper position, return new max

# child node index/2 = parent node index

class MaxHeap:
	def __init__(self,items=[]):
		self.heap = [0]

		# In case there are multiple items to add to the heap upon instancing...
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap)-1)

	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap)-1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False

	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1,len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max

	def __swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self,index):
		parent = index/2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[index]:
			self.__swap(index,parent)
			self.__floatUp(parent)

	def __bubbleDown(self,index):
		left = index * 2
		right = index * 2 + 1
		largest = index

		if len(self.heap) > left and self.heap[largest]





		