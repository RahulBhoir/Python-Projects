class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:

    def __init__(self):
        self.head = None

    def Insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next is None:
                    break
                temp = temp.next  # temp is pointing to the next node
            temp.next = newNode

        def InsertByPosition(self, newNode, position):
            count = linklist.countNode()
        if position == 1:
            temp = self.head
            self.head = newNode
            self.head.next = temp
        else:
            temp = self.head
            for i in range(position - 2):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

    def Delete(self, position):
        temp = self.head
        for i in range(position - 2):
            temp = temp.next
        temp2 = temp.next
        temp.next = temp2.next

    def printNode(self):
        if self.head is None:
            print("list is empty :(")
            return
        temp = self.head
        while True:
            print(temp.data, "->", end="")
            if temp.next is None:
                print("NUll")
                break
            temp = temp.next

    def countNode(self, count):
        temp = self.head
        count = 0
        while (temp.next is not None):
            temp = temp.next
            count += 1
        print("length of list is ", count)


list = linklist()

while True:
    print()
    print("select from the options below\n1.Insert at end\n2.Insert by position\n3.Delete\n4.Print\n5.Exit\n6.Length of List")
    n = int(input("choice: "))
    print()
    if n == 1:
        for i in range(int(input("enter the numbers of node: "))):
            list.Insert(Node(input("enter the node value: ")))
            continue
    elif n == 2:
        newNode = Node(input("enter the node value: "))
        position = int(input("enter the node position:"))
        list.InsertByPosition(newNode, position)
        continue
    elif n == 3:
        list.Delete(int(input("enter the node position to be deleted:")))
        continue
    elif n == 4:
        list.printNode()
        continue
    elif n == 5:
        break
    elif n == 6:
        list.countNode()
        continue
    else:
        print("plz enter valid choice\n")
        continue
