# First solution is keeping track of the min value for every action on the stack.
# Inefficient, but is still a solution

class StackMin:
    def __init__(self):
        self.items = []
        self.currentMin = None

    def push(self, item):
        self.items.append(item)
        self.currentMin = self.get_min()

    def pop(self):
        self.items.pop()
        self.currentMin = self.get_min()

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

    def get_min(self):
        if self.items == []:
            raise Exception ("This is an empty stack.")
        self.currentMin = min(self.items)
        return self.currentMin

testStack = StackMin()
testStack.push(4)
testStack.push(2)
testStack.push(3)
testStack.push(1)
testStack.push(5)
testStack.push(6)
testStack.pop()
testStack.pop()
testStack.pop()

testStack.get_stack()
print(testStack.get_min())