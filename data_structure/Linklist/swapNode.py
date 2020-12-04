class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        
    def InsertLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode

    def SwapNode(self, data1, data2):
        temp = self.head
        if self.head is data1:
            temp1 = self.head
            

