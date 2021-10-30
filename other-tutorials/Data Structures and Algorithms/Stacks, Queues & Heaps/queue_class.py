# First in, First out
# Enqueue - add an item at the end of the queue
# Dequeue - remove an item at the front of the queue

class Queue:
	def __init__(self):
		self.queue = []

	# Enqueue a value to the queue
	def enqueue(self,value):
		self.queue.append(value)

	# Dequeue the first value in the queue
	def dequeue(self):
		if len(self.queue) >= 1:
			return self.queue.pop(0)
		else:
			return None

	# Get the size of the whole queue
	def get_size(self):
		return len(self.queue)