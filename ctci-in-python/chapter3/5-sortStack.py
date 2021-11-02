# Sort a stack such that the smallest items are at the top
# Can't use other data structures to store items temporarily except additional stack
# Only use peek, push, pop, is_empty

class MyStack:
    def __init__(self):
        self.items = []
        self.ordered_stack = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        print("The whole stack:", self.items)
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            print("Current Top of the Stack:", self.items[-1])
            return self.items[-1]

    def sort_stack(self):
        # TODO: Sort the stack

        return True

test_stack = MyStack()
test_stack.push(5)
test_stack.push(1)
test_stack.push(4)
test_stack.push(3)
test_stack.push(2)
test_stack.push(7)
test_stack.push(6)
test_stack.get_stack() # Should get [5,1,4,3,2,7,6]

test_stack.sort_stack()
test_stack.get_stack() # Should get [1,2,3,4,5,6,7]