from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"({self.value})"


class LinkedList:
    def __init__(self):
        self.nodes: List[Node] = []

    def append(self, node: Node):
        self.nodes.append(node)
        return self

    def __repr__(self):
        return " -> ".join([str(node) for node in self.nodes]) + " -> " + "None"


linked_list = LinkedList()
linked_list.append(Node(10)).append(Node(20)).append(Node(30))


print(linked_list)