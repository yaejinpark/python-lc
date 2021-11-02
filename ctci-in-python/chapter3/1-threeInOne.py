# Easier Solution: Stack sizes are fixed (issue of empty stacks or overflow)
class ThreeInOneFixed:
    def __init__(self, stack_capacity):
        self.num_stacks = 3
        self.stack_capacity = stack_capacity # How many elements can a stack hold?
        self.stack_values = [0] * stack_capacity * self.num_stacks # Capacity of each stacks
        self.stack_sizes = [0] * self.num_stacks # List of the three stack sizes within the stack

    def is_empty(self, stack_num):
        return self.stack_sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.stack_sizes[stack_num] == self.stack_capacity

    def top_index(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.stack_sizes[stack_num]

        return offset + size - 1

    def push(self, stack_num, data):
        if self.is_full(stack_num):
            raise Exception ('The stack is already full.')
        self.stack_sizes[stack_num] += 1 # Increase the size of the stack
        top_index = self.top_index(stack_num) # Get the top index
        self.stack_values[top_index] = data # Stack the data onto the top of the stack

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception ('The stack is already empty.')
        top_index = self.top_index(stack_num)
        value = self.stack_values[top_index] # Get the top of the stack
        self.stack_values[top_index] = 0 # Clear the top
        self.stack_sizes[stack_num] -= 1

        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception ('Stack is empty, nothing to peek.')
        print(self.stack_values[self.top_index(stack_num)])
        return self.stack_values[self.top_index(stack_num)]

    def get_stacks(self):
        print(self.stack_values)

test_data = ThreeInOneFixed(3)
test_data.push(1,1)
test_data.get_stacks()
test_data.peek(1)
test_data.push(2,2)
test_data.get_stacks()
test_data.pop(2)
test_data.get_stacks()