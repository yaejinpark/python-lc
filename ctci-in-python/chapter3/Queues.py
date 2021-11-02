# Useful for caches or in BFS

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        print("Popped item:", self.queue[0])
        self.queue.pop(0)

    def get_queue(self):
        print("Current Queue:", self.queue)
        return self.queue

    def is_empty(self):
        return self.queue == []

    def get_size(self):
        print("Queue size:", len(self.queue))
        return len(self.queue)

testQueue = Queue()
testQueue.push("A")
testQueue.push("B")
testQueue.push("C")
testQueue.push("D")

testQueue.get_queue() # Should get [A B C D]

testQueue.pop()
testQueue.get_queue() # Should get [B C D]

testQueue.is_empty() # False

testQueue.get_size() # Should be 3