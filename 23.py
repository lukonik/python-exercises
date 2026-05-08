from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[-1]
        self.data = self.data[:-1]
        return item

    def peek(self):
        return self.data[-1]


stack = Stack()

stack.push("pynative.com")
stack.push("facebook.com")
stack.push("google.com")

print(stack.peek())
print(stack.pop())

print(stack.data)
