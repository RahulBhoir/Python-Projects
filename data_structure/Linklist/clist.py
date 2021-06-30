class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None

    def Insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while True:
                if temp.next is self.head:
                    break
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def printList(self):
        temp = self.head
        while True:
            print(temp.data, "->", end="")
            if temp.next is self.head:
                print("head")
                break
            temp = temp.next

    def deleteNode(self, n):
        temp = self.head
        prev = self.head
        if n == 1:
            while True:
                if prev.next is temp:
                    break
                prev = prev.next
            self.head = self.head.next
            prev.next = self.head
            return
        for i in range(n - 2):
            temp = temp.next
        temp1 = temp.next
        temp.next = temp1.next


list = CircularLinkList()

list.Insert(1)
list.Insert(4)
list.Insert(2)

list.printList()
list.deleteNode(3)
list.printList()
