from linklist import Node, linklist
def merge(list1, list2, mergelist):
    c1 = list1.head
    c2 = list2.head
    while True:
        if c1 is None:
            mergelist.Insert(c2)
            break
        
        if c2 is None:
            mergelist.Insert(c1)
            break

        if c1.data < c2.data:
            temp = c1.next
            c1.next = None
            mergelist.Insert(c1)
            c1 = temp
        else:
            temp = c2.next
            c2.next = None
            mergelist.Insert(c2)
            c2 = temp


list1 = linklist()
list2 = linklist()

list1.Insert(Node(1))
list1.Insert(Node(3))
list1.Insert(Node(4))

list2.Insert(Node(2))
list2.Insert(Node(5))
list2.Insert(Node(7))

list1.printNode()
list2.printNode()

mergelist = linklist()

merge(list1, list2, mergelist)

mergelist.printNode()
