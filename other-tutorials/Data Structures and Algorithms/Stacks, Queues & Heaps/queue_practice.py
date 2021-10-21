import queue_class as queue

myqueue = queue.Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.get_size())