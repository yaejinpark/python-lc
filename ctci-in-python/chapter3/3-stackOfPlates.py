# Start another dish stack if the stack reaches its threshold

class SetOfStacks:
    def __init__(self, capacity):
       self.stack_set=[] # List in a list
       self.capacity = capacity

    def push(self, item):
        # If the stack set is empty, append an empty stack in the stack set
        if len(self.stack_set) == 0:
            self.stack_set.append([])

        # If the stack_set is not empty and the last set is not full yet, fill that set
        if self.stack_set and len(self.stack_set[-1]) < self.capacity:
            self.stack_set[-1].append(item)

        # Else if the last set is full, append a new stack with the desired item.
        else:
            self.stack_set.append([item])

        return self.stack_set

    def pop(self):
        # If the last stack in the set is empty, delete the whole stack
        if len(self.stack_set[-1]) == 0:
            del self.stack_set[-1]
        # Else, pop the last item in the last stack
        else:
            self.stack_set[-1].pop()
        return self.stack_set

    #Follow up: pop at a specific substack
    def popAt(self, index):
        if self.stack_set[index] == []:
            del self.stack_set[index]
        else:
            self.stack_set[index].pop()

    def get_stack(self):
        print(self.stack_set)

testStack = SetOfStacks(3)
testStack.push(1)
testStack.push(2)
testStack.push(3)
testStack.push(4)
testStack.push(5)
testStack.push(6)
testStack.push(7)
testStack.push(8)
testStack.push(9)
testStack.push(10)

testStack.get_stack() # Should get [[1,2,3],[4,5,6],[7,8,9],[10]]

testStack.pop()
testStack.pop()
testStack.pop()

testStack.get_stack() # Should get [[1,2,3],[4,5,6],[7,8]

testStack.popAt(1)

testStack.get_stack() # Should get [[1,2,3],[4,5],[7,8]
