from single_ll_extra_functions import (NthNodeFromLast, MiddleNode,
                                       CountTheElement, RemoveDuplicates)


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        temp = self.head
        counter = 0
        while temp != None:
            if counter == index:
                return temp.val
            counter += 1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        next_node = self.head
        self.head = new_node
        new_node.next = next_node
        return

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        new_node = Node(val)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head is None or index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        temp = self.head
        counter = 0
        while temp.next != None:
            counter += 1
            if counter == index:
                next_node = temp.next
                temp.next = new_node
                new_node.next = next_node
            temp = temp.next
        # If index equals the length of the linked list,
        # the node will be appended to the end of the linked list
        if counter+1 == index:
            temp.next = new_node
        return

    def deleteAtIndex(self, index: int):
        if self.head is None:
            return
        temp = self.head
        counter = 0
        if counter == index:
            self.head = self.head.next
            return
        while temp.next != None:
            if counter + 1 == index:
                next_node = temp.next.next
                temp.next = next_node
                return
            counter += 1
            temp = temp.next
        return

    def PrintValues(self):
        if self.head is None:
            return 'list is empty :('
        print('Element in LL are:')
        temp = self.head
        while temp != None:
            print(temp.val, end=' ')
            temp = temp.next
        print()
        return

    def FindLength(self, temp):
        if temp is None:
            return 'list is empty :('
        if temp.next is None:
            return 1

        length = self.FindLength(temp.next)
        length += 1
        return length

    def FindElement(self, temp, val):
        if temp is None:
            return 'list is empty :('
        if temp.val is val:
            return True
        is_present = self.FindElement(temp.next, val)
        return True if is_present is True else False


# 1 -> 2 -> 3 -> 4 -> None
obj = MyLinkedList()
obj.get(0)
obj.addAtHead(10)
obj.addAtHead(10)
obj.addAtHead(10)
obj.addAtIndex(3, 20)
obj.addAtIndex(4, 30)
obj.addAtIndex(5, 30)
obj.addAtTail(30)
obj.addAtTail(50)
obj.addAtTail(50)
obj.PrintValues()
print('The length of LL is:', obj.FindLength(obj.head))
print('The element 30 is present?', obj.FindElement(obj.head, 30))
obj.PrintValues()
print('The element from the end of the LL at node 3 is:',
      NthNodeFromLast(obj.head, 3))
# print(MiddleNode(obj.head))
print('Count of 30 is:', CountTheElement(obj.head, 30))
RemoveDuplicates(obj.head)
print('the sorted list is')
obj.PrintValues()
