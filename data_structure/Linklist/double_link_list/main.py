from dListFunctions import PrintValues, ReverseList

from dListFunctions import LIST_IS_EMPTY


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None


class DoubleLinkList():
    def __init__(self) -> None:
        self.head = None

    def InsertNodeAtTail(self, data):
        if self.head is None:
            self.InsertAtHead(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # delete node by value
    def DeleteNode(self, val):
        if self.head is None:
            return LIST_IS_EMPTY
        if self.head.val == val:
            self.head = self.head.next
            return
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.val == val:
                    prev_node = temp.next.prev
                    next_node = temp.next.next
                    temp.next = next_node
                    if next_node is not None:
                        next_node.prev = prev_node
                        return
                    return
                temp = temp.next
        return

    def InsertAtHead(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
        return


obj = DoubleLinkList()
obj.InsertAtHead(5)
obj.InsertNodeAtTail(1)
obj.InsertNodeAtTail(2)
obj.InsertNodeAtTail(3)
obj.InsertNodeAtTail(4)
PrintValues(obj.head)
obj.DeleteNode(4)
PrintValues(obj.head)
obj.InsertAtHead(56)
PrintValues(obj.head)
obj.head = ReverseList(obj.head)
PrintValues(obj.head)