# Stack functions using linklist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            newNode.next = None
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            return "underflow"
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp

    def peek(self):
        if self.top is None:
            return "underflow"
        else:
            return self.top.data

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print("null")
