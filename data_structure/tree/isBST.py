root = None
max_value = 100000
min_value = -100000


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root, min_value, max_value):
    if root is None:
        return True
    if (root.data < max_value and root.data > min_value and
            isBST(root.left, min_value, root.data) and isBST(root.right, root.data, max_value)):
        return True
    else:
        return False


root = Node(11)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(12)
root.right.right = Node(15)
root.right.right.left = Node(14)
tree = isBST(root, min_value, max_value)
print(tree)
