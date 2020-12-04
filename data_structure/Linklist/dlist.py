class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            temp = self.head
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

    def prepend(self, data):
        temp = self.head
        new_node = Node(data)
        self.head = new_node
        new_node.prev = None
        new_node.next = temp

    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.data, '->', end='')
            temp = temp.next
        print("null")

    def delete(self, n):
        if n == 1:
            temp = self.head.next
            self.head = temp
            self.head.prev = None
        else:
            temp = self.head
            for i in range(n - 1):
                temp = temp.next
            if temp.next is None:
                temp1 = temp.prev
                temp1.next = None
                return
            temp1 = temp.prev
            temp2 = temp.next
            temp1.next = temp2
            temp2.prev = temp1


list1 = DoublyLinkList()

list1.append(1)
list1.append(3)
list1.append(2)

list1.prepend(8)
list1.printlist()

list1.delete(4)
list1.printlist()
