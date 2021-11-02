# Problem link: https://www.codewars.com/kata/55beec7dd347078289000021/train/python

# Implement Length() to count the number of nodes in a linked list.
# Implement Count() to count the occurrences of an integer in a linked list.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):    
    if node is None: # If there is no current node, length is 0
        return 0
    
    current = node
    counter = 1
    
    while current.next is not None:
        counter += 1
        current = current.next # Iterate through LL and count the nodes
    return counter
  
def count(node, data):
    if node is None:
        return False
    
    current = node
    frequency = {} # Dictionary for storing node data and frequency as kv pair
    
    while current is not None:
        if current.data in frequency:
            frequency[current.data] += 1 # If node data already in dictionary, increase frequency
        else:
            frequency[current.data] = 1 # If node data not in dictionary, add as new kv pair
        current = current.next    
    
    if data in frequency: # Return the frequency of data if data exists in dictionary
        return frequency[data]
    else:
        return 0 # Return 0 if the data does not exist in frequency