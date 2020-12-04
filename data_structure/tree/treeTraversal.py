root = None


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Insert(root, data):
    if root is None:
        root = Node(data)
        return root
    elif data <= root.data:
        root.left = Insert(root.left, data)
    return root


def Infix(root):
    if root:
        Infix(root.left)
        print(root.data, end=' ')
        Infix(root.right)


def Prefix(root):
    if root:
        print(root.data, end=' ')
        Prefix(root.left)
        Prefix(root.right)


def Postfix(root):
    if root:
        Postfix(root.left)
        Postfix(root.right)
        print(root.data, end=' ')


root = Node(10)
root.left = Node(9)
root.right = Node(12)
Infix(root)
print()
Prefix(root)
print()
Postfix(root)
