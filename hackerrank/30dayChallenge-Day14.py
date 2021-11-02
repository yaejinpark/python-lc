class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference (self):
        sortedArray = sorted(self.__elements)
        self.maximumDifference = sortedArray[len(sortedArray)-1] - sortedArray[0]
        return self.maximumDifference