# Implement a queue with two stacks.

class MyQueue:
    def __init__(self):
        self.stack_oldest = []
        self.stack_newest = []

    def push(self, item):
        self.stack_newest.append(item)

    # Shift stacks from new to old by appending popped items from new into the old
    # This guarantees that the values are now in reverse ordered stack
    # Repeat until new stack is empty
    def new_to_old(self):
        if self.stack_oldest == []:
            while self.stack_newest != []:
                self.stack_oldest.append(self.stack_newest.pop())

    def pop(self):
        # If oldest stack has some values left, pop them first
        if len(self.stack_oldest) > 0:
            self.stack_oldest.pop()
        # If oldest stack is empty, make sure the shift of values from newest to oldest stack happens first
        # Then pop the old stack
        else:
            self.new_to_old()
            self.stack_oldest.pop()

    # For printing the stack
    def get_queue(self):
        if self.stack_oldest == []:
            print(self.stack_newest)
        else:
            print(self.stack_oldest[::-1])

test_queue = MyQueue()
test_queue.push(1)
test_queue.push(2)
test_queue.push(3)
test_queue.push(4)
test_queue.push(5)
test_queue.push(6)
test_queue.push(7)
test_queue.push(8)
test_queue.get_queue() # Should print [1,2,3,4,5,6,7,8]

test_queue.pop()
test_queue.pop()

test_queue.get_queue() # Should print [3,4,5,6,7,8]
