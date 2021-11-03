# This class is for creating arrays of random integers.
# Lengths and maximum integer can be chosen

from random import randint

class IntegerArray:
	def __init__(self,length,maxint):
		self.length = length
		self.maxint = maxint

	def create_array(self):
		arr = [randint(0,self.maxint) for _ in range(self.length)]
		print(f"Your new integer array is: {arr}")
		return arr