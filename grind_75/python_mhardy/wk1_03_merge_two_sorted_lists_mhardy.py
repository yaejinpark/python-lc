# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]



# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-100) # the 'ultimate' head, previous of the starting point
        prev_node = head

        while list1 and list2:
            if list1.val <= list2.val: # if list 1's node is smaller, set pointer to list 1's node
                prev_node.next = list1
                list1 = list1.next
            elif list2.val < list1.val: # if list 2's node is smaller, set pointer to list 2's node
                prev_node.next = list2
                list2 = list2.next
            prev_node = prev_node.next # move onto the next node that has been appended
        
        prev_node.next = list1 or list2 # append the longer linked list that still remains, if any
        return head.next
