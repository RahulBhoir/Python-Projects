from list_functions import (NthNodeFromLast, MiddleNode,
                            CountTheElement, RemoveDuplicates,
                            CheckLoop, ReverseList, LastElementToFirst, PrintValues)


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def listIsEmpty(self):
        if self.head == None:
            return True

    def get(self, index: int) -> int:
        if self.listIsEmpty():
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
        new_node.next = self.head
        self.head = new_node
        return

    def addAtTail(self, val: int) -> None:
        if self.listIsEmpty():
            self.addAtHead(val)
            return
        new_node = Node(val)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if self.listIsEmpty() or index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        temp = self.head
        counter = 0
        while temp.next != None:
            counter += 1
            if counter == index:
                new_node.next = temp.next
                temp.next = new_node
            temp = temp.next
        # If index equals the length of the linked list,
        # the node will be appended to the end of the linked list
        if counter+1 == index:
            temp.next = new_node
        return

    def deleteAtIndex(self, index: int):
        if self.listIsEmpty():
            return
        temp = self.head
        counter = 0
        # deleting the first element
        if counter == index:
            self.head = self.head.next
            return
        #  for rest of the elements
        while temp.next != None:
            if counter + 1 == index:
                temp.next = temp.next.next
                return
            counter += 1
            temp = temp.next
        return

# recursive approach
    def FindLength(self, temp):
        if temp is None:
            return 0
        if temp.next is None:
            return 1
# 1 -> 2 -> null
        length = self.FindLength(temp.next)
        length += 1
        return length

    def FindElement(self, temp, val):
        if temp is None:
            return 'list is empty :('
        if temp.val == val:
            return True
        is_present = self.FindElement(temp.next, val)
        return True if is_present == True else False


# reverse ll using recursion

    def reverseList(self):
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


# 1 -> 2 -> 3 -> 4 -> None
obj = MyLinkedList()
# obj.get(0)
# obj.addAtHead(10)
# obj.addAtHead(10)
# obj.addAtHead(10)
# obj.addAtIndex(3, 20)
# obj.addAtIndex(4, 30)
# obj.addAtIndex(5, 30)
obj.addAtTail(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
# obj.addAtTail(50)
# obj.addAtTail(50)
# obj.PrintValues()
print('The length of LL is:', obj.FindLength(obj.head))
print('Is element 30 present in the list?', obj.FindElement(obj.head, 4))
# obj.PrintValues()
print(f'Nth node is:', NthNodeFromLast(obj.head, 1))
# # print(MiddleNode(obj.head))
# print('Count of 30 is:', CountTheElement(obj.head, 30))
# RemoveDuplicates(obj.head)
# print('the sorted list is')
# PrintValues(obj.head)
# print('is there a loop in the linked list?', CheckLoop(obj.head))
# print(Palindrome(obj.head, obj.head))
# obj.head = ReverseList(obj.head)
# obj.PrintValues()
obj.head = LastElementToFirst(obj.head)
PrintValues(obj.head)
