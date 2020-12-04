root = None


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def MinNode(root):
    if root is None:
        return
    if root.left is None:
        print(root.data)
        return
    MinNode(root.left)


def MaxNode(root):
    if root is None:
        return
    if root.right is None:
        print(root.data)
        return
    MaxNode(root.right)


root = Node(11)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(12)
root.right.right = Node(15)
MaxNode(root)
MinNode(root)
