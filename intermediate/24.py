from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.append(item)

    def deque(self):
        return self.buffer.popleft()
    
queue = Queue()

queue.enqueue("Customer A")
queue.enqueue("Customer B")
queue.enqueue("Customer C")

print(queue.buffer)

print(queue.deque())

print(queue.buffer)
