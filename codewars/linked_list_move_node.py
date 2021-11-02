# Problem link: https://www.codewars.com/kata/55da347204760ba494000038/train/python

# Write a MoveNode() function which takes the node from the front of the source list and moves it to the front of the destintation list. 
# You should throw an error when the source list is empty.

# source = 1 -> 2 -> 3 -> None
# dest = 4 -> 5 -> 6 -> None
# move_node(source, dest).source == 2 -> 3 -> None
# move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):    
    if dest == None:
        # Case 1: Both source and dest are empty - throw error
        if source == None:
            raise ValueError
            
        # Case 2: Source is not empty but Dest is - set source to dest
        else:
            moving_node = source # Save the node I want to move in moving_node
            source = source.next # Set the moved node in source LL to None
            dest = moving_node
            dest.next = None
    else:
        # Case 3: Dest is not empty but Source is - throw error
        if source == None:
            raise ValueError
            
        # Case 4: Dest and Source are both not empty - Set dest's head to source and push all nodes in dest
        else:
            moving_node = source
            source = source.next
            
            moving_node.next = dest
            dest = moving_node            
    
    # Remember to return the context.
    return Context(source, dest)