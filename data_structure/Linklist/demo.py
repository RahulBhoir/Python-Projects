class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def InsertFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def InsertMiddle(self, prev_data, data):
        if self.head is None:
            print("No previous node")
            return

        newNode = Node(data)
        temp = self.head
        while temp.data != prev_data:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def InsertLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode

    def DeleteNode(self, data):
        if self.head.data is data:
            self.head = self.head.next
            return

        temp = self.head
        while temp is not None:
            if temp.next.data == data:
                break
            temp = temp.next
        temp.next = temp.next.next

    def DeletePosition(self, pos):
        if self.head is None:
            print("list is empty")
            return
        elif pos == 0:
            self.head = self.head.next
            return
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            temp.next = temp.next.next

    def ListLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print('length of list is:', count)

    def PrintNode(self):
        head = self.head
        while head != None:
            print(head.data, " ")
            head = head.next

    def SwapData(self, data1, data2):
        temp = self.head
        while temp is not None:
            if temp.data == data1:
                temp.data = data2
            elif temp.data == data2:
                temp.data = data1
            temp = temp.next


p = LinkedList()
p.InsertLast(1)
p.InsertFirst(89)
p.InsertLast(6)
p.InsertLast(9)
p.InsertLast(8)
p.InsertMiddle(9, 2)
p.PrintNode()
p.ListLength()
print('after deleting')
# p.DeleteNode(8)
# p.DeleteNode(89)
# p.DeletePosition(5)
p.PrintNode()
p.ListLength()
p.SwapData(89, 8)
p.PrintNode()
