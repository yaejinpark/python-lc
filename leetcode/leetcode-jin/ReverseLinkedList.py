# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listPrev = None
        listNext = None
        listCurrent = head

        while (listCurrent != None):
            listNext = listCurrent.next
            listCurrent.next = listPrev
            listPrev = listCurrent
            listCurrent = listNext

        return listPrev