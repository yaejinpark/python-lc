# Problem link: https://www.codewars.com/kata/582c297e56373f0426000098/train/python
# Given:

# class Node():
	# def __init__(self, data, next = None):
	#     self.data = data
	#     self.next = next

def stringify(node):
    this_node = node
    res = ""
    
    while this_node is not None:
        res += str(this_node.data) + ' -> '
        this_node = this_node.next

    return res+"None"