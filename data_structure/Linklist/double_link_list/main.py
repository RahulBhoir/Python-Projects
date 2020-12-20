from dListFunctions import PrintValues

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
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

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


obj = DoubleLinkList()
obj.InsertNodeAtTail(1)
obj.InsertNodeAtTail(2)
obj.InsertNodeAtTail(3)
obj.InsertNodeAtTail(4)
PrintValues(obj.head)
obj.DeleteNode(4)
PrintValues(obj.head)
