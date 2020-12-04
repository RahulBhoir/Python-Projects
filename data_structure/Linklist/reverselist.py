from linklist import Node, linklist

def Reverse(list1):
    temp = list1.head
    prev = None
    next = None
    
    while temp != None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    list1.head = prev


list1 = linklist()

list1.Insert(Node(1))
list1.Insert(Node(2))
list1.Insert(Node(3))
list1.Insert(Node(4))

list1.printNode()

Reverse(list1)

list1.printNode()