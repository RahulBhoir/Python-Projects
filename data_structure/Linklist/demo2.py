class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LL():
    def __init__(self):
        self.head = None

    def InsertNode(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    def InsertFirst(self, data):
        newNode = Node(data)
        temp = self.head
        self.head = newNode
        newNode.next = temp

    def InsertPostion(self, data, prev_node):
        if prev_node is None:
            return 'node not in list'
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode

    def PrintNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    # def ReverseList(self):
    #     print('reverse list')
    #     current = self.head
    #     prev = None
    #     while current != None:
    #         nextNode = current.next
    #         current.next = prev
    #         prev = current
    #         current = nextNode
    #     self.head = prev

    def DeleteNode(self, data):
        if self.head is None:
            return "list is empty"
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        temp.next = temp.next.next

    def ReverseList(self):
        print('reverse list')
        self.reverse(self.head)

    def reverse(self, temp):
        if temp.next is None:
            self.head = temp
            return
        self.reverse(temp.next)
        temp2 = temp.next
        temp2.next = temp
        temp.next = None


# 1->2->56
l = LL()
l.InsertFirst(78)
l.InsertNode(1)
l.InsertNode(2)
l.InsertNode(56)
l.InsertFirst(12)
l.InsertPostion(15, l.head.next)
l.PrintNode()
# l.ReverseList()
# l.PrintNode()
print()
l.DeleteNode(56)
l.PrintNode()
