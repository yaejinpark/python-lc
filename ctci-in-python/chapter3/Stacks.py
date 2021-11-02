class StackNode:
    def __init__(self, item = 0):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.items = []

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

    def get_size(self):
        print("Stack Size:", len(self.items))
        return len(self.items)

def stack_test():
    testStack = Stack()
    testStack.push("A")
    testStack.push("B")
    testStack.push("C")
    testStack.push("D")
    testStack.get_stack() # Should print [A, B, C, D]

    testStack.peek() # Should print D

    testStack.get_size() # Should print 4

    testStack.pop()
    testStack.get_stack() # Should print [A, B, C]

# stack_test()
