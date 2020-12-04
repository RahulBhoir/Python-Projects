root = None


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def FindMin(root):
    print(root.data)
    if root is None:
        return root
    if root.left is None:
        return root
    temp = FindMin(root.left)
    return temp


def DeleteNode(root, data):
    if root is None:
        return root
    elif root.data > data:
        root.left = DeleteNode(root.left, data)
    elif root.data < data:
        root.right = DeleteNode(root.right, data)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            temp = FindMin(root.right)
            root.data = temp.data
            print(temp.data)
            root.right = DeleteNode(root.right, temp.data)
    return root


def Prefix(root):
    if root:
        print(root.data, end=' ')
        Prefix(root.left)
        Prefix(root.right)


root = Node(11)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(12)
root.right.right = Node(15)
root.right.right.left = Node(14)
Prefix(root)
DeleteNode(root, 13)
Prefix(root)
