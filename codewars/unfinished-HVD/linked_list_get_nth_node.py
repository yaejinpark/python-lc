# Problem Link: https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/python
# Linked Lists - Get Nth

# Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. 
# GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. 
# So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
def get_nth(node, index):
    # Your code goes here.
    this_node = node

    if index < 0:
        raise IndexError
    
    if this_node == None:
        raise ValueError
    
    i = 0
    
    while i in range(index):
        this_node = this_node.next
        if this_node == None:
            raise ValueError
        i += 1