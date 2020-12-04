root = None


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def FindHeight(root):
    if root is None:
        return -1
    left_height = FindHeight(root.left)
    right_height = FindHeight(root.right)
    return max(left_height, right_height)+1


root = Node(11)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(12)
root.right.right = Node(15)
root.right.right.left = Node(14)
height = FindHeight(root)
print(height)
