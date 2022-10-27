# https://www.codewars.com/kata/55d17ddd6d7868493e000074/train/python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    # Remember to return the head of the list.
    if not listA and not listB: return None
    if not listA: return listB
    if not listB: return listA
    
    head = listA
    current = head
    
    while current.next != None:
        current = current.next
    
    current.next = listB
    return head