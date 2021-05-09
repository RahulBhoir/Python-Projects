from main import MyLinkedList
from list_functions import PrintValues


def merge(list1, list2, mergelist):
    c1 = list1.head
    c2 = list2.head
    while True:
        if c1 is None:
            mergelist.addAtTail(c2.data)
            break

        if c2 is None:
            mergelist.addAtTail(c1.data)
            break

        if c1.val < c2.val:
            temp = c1.next
            c1.next = None
            mergelist.addAtTail(c1.val)
            c1 = temp
        else:
            temp = c2.next
            c2.next = None
            mergelist.addAtTail(c2.val)
            c2 = temp


def addAllElements(listHead, mergeList):
    while listHead != None:
        mergeList.addAtTail(listHead.val)
        listHead = listHead.next


def mergeTwoList(list1, list2, mergeList):
    h1 = list1.head
    h2 = list2.head
    if h1 is None:
        mergeList = h2
        return
    if h2 is None:
        mergeList = h1
        return

    while True:
        if h1 is None:
            addAllElements(h2, mergeList)
            return
        if h2 is None:
            addAllElements(h1, mergeList)
            return
        if h1.val < h2.val:
            mergeList.addAtTail(h1.val)
            h1 = h1.next
        else:
            mergeList.addAtTail(h2.val)
            h2 = h2.next


list1 = MyLinkedList()
list2 = MyLinkedList()

list1.addAtTail(1)
list1.addAtTail(3)
list1.addAtTail(4)

list2.addAtTail(2)
list2.addAtTail(5)
list2.addAtTail(7)

PrintValues(list1.head)
PrintValues(list2.head)

mergeList = MyLinkedList()

mergeTwoList(list1, list2, mergeList)

PrintValues(mergeList.head)
