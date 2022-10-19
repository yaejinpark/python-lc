# Linked Lists - Append

# Write an Append() function which appends one linked list to another. 
# The head of the resulting list should be returned.

# var listA = 1 -> 2 -> 3 -> null
# var listB = 4 -> 5 -> 6 -> null
# append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# If both listA and listB are null/NULL/None/nil, return null/NULL/None/nil. 
# If one list is null/NULL/None/nil and the other is not, simply return the non-null/NULL/None/nil list.

# The push() and buildOneTwoThree() (build_one_two_three() in PHP and ruby) functions need not 
# be redefined. The Node class is also predefined for you in PHP.

# /* PHP Only */
# class Node {
#   public $data, $next;
#   public function __construct($data, $next = NULL) {
#     $this->data = $data;
#     $this->next = $next;
#   }
# }


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if not listA and not listB:
        return None
    elif not listA and listB:
        return listB
    elif listA and not listB:
        return listA
    else:
        head = listA
        current = listA
        while current.next != None:
            current = current.next
        current.next = listB
    
        return head

import codewars_test as test

def push(head, data):
  newNode = Node(data)
  newNode.next = head
  return newNode

def build_one_two_three():
  head = None
  head = push(head, 3)
  head = push(head, 2)
  head = push(head, 1)  
  return head

def build_four_five_six():
  head = None
  head = push(head, 6)
  head = push(head, 5)
  head = push(head, 4)
  return head

def build_one_two_three_four_five_six():
  head = None
  head = push(head, 6)
  head = push(head, 5)
  head = push(head, 4)
  head = push(head, 3)
  head = push(head, 2)
  head = push(head, 1)
  return head

def build_four_five_six_one_two_three():
  head = None
  head = push(head, 3)
  head = push(head, 2)
  head = push(head, 1)
  head = push(head, 6)
  head = push(head, 5)
  head = push(head, 4)
  return head

def build_one_two():
  head = None
  head = push(head, 2)
  head = push(head, 1)
  return head

def build_two_one():
  head = None
  head = push(head, 1)
  head = push(head, 2)
  return head
  
def assert_linked_list_equals(listA, listB, message):
  while listA is not None and listB is not None:
    test.assert_equals(listA.data, listB.data, message)
    listA = listA.next
    listB = listB.next
  test.assert_equals(listA, None, message)
  test.assert_equals(listB, None, message)

@test.describe("Tests") 
def te():
    @test.it("should be able to handle two empty lists.")
    def f():
        test.assert_equals(append(None, None), None, "appending two empty lists should return None.")
    
    @test.it("should be able to handle one empty list and one non-empty list.")
    def f():
        assert_linked_list_equals(append(None, build_one_two_three()), build_one_two_three(), "appending a list to None should return the list.")
        assert_linked_list_equals(append(build_one_two_three(), None), build_one_two_three(), "appending None to a list should return the list.")
    
    @test.it("should be able to handle two non-empty lists of length 1.")
    def f():
        assert_linked_list_equals(append(Node(1), Node(2)), build_one_two(), "appending a list to another list should return the concatenated list.")
        assert_linked_list_equals(append(Node(2), Node(1)), build_two_one(), "appending a list to another list should return the concatenated list.")
        assert_linked_list_equals(append(Node(2), Node(1)).next.next, None, "None should exist at end of concatenated linked list.")
    
    @test.it("should be able to handle two non-empty lists of length > 1.")
    def f():
        assert_linked_list_equals(append(build_one_two_three(), build_four_five_six()), build_one_two_three_four_five_six(), "appending a list to another list should return the concatenated list.")
        assert_linked_list_equals(append(build_four_five_six(), build_one_two_three()), build_four_five_six_one_two_three(), "appending a list to another list should return the concatenated list.")
        assert_linked_list_equals(append(build_four_five_six(), build_one_two_three()).next.next.next.next.next.next, None, "None should exist at end of concatenated linked list.")