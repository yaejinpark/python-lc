class Stack():
	# Stack constructor - create an empty list
	def __init__(self):
		self.stack = list()
	
	# Push a new value into stack
	def push(self,value):
		self.stack.append(value)

	# Pop the last value of the stack
	def pop(self):
		if len(self.stack) >= 1:
			return self.stack.pop()
		else:
			return None

	# Peek - see the very last value of stack
	def peek(self):
		if len(self.stack) > 0:
			return self.stack[len(self.stack)-1]
		else:
			return None