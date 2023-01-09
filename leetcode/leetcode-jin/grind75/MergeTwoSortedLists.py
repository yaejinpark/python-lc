# https://leetcode.com/problems/merge-two-sorted-lists/description/
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