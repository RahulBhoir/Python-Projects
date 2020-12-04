root = None


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LevelOrder(root):
    Q = []
    if root is None:
        print('empty tree')
        return
    Q.append(root)
    while len(Q) != 0:
        temp = Q.pop(0)
        print(temp.data, end=' ')
        if temp.left:
            Q.append(temp.left)
        if temp.right:
            Q.append(temp.right)


root = Node(11)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(7)
root.left.right = Node(10)
root.right.left = Node(12)
root.right.right = Node(15)
root.right.right.left = Node(14)
# height = FindHeight(root)
# print(height)
LevelOrder(root)
