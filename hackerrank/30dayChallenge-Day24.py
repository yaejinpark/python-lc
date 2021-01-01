#Find duplicates in a linked list and 'delete' them

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head == None or head.next == None:
            return head

        current = head
        while current.next:
            #If data is duplicate, move the next node's pointer to next's next
            if current.data == current.next.data:
                current.next = current.next.next
            #If data is not duplicate, move on
            else:
                current = current.next
        return head