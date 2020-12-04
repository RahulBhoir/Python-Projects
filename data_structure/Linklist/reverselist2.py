from linklistFunct import Node, linklist


def reverseList(list1):
    temp1 = list1.head

    def reverse(temp):
        if temp is None:
            head = temp
            return
        reverse(temp.next)
        q = temp.next
        q.next = temp
        temp.next = None


list1 = linklist()
list1.Insert(Node(1))
list1.Insert(Node(2))
list1.Insert(Node(3))
list1.Insert(Node(4))

list1.printNode()

reverseList(list1)
list1.printNode()
