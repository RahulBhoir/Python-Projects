class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def BottomView(root, distance, level):
    elements = dict()

    def GetBottomView(root, distance, level):
        if root is None:
            return
        if distance not in elements or elements[distance]['level'] < level:
            elements[distance] = {'value': root.data, 'level': level}
        GetBottomView(root.left, distance - 1, level + 1)
        GetBottomView(root.right, distance + 1, level + 1)
    GetBottomView(root, distance, level)
    print('Bottom View: ', end=' ')
    PrintView(elements)


def TopView(root, distance, level):
    elements = dict()

    def GetTopView(root, distance, level):
        if root is None:
            return
        if distance not in elements or elements[distance]['level'] > level:
            elements[distance] = {'value': root.data, 'level': level}
        GetTopView(root.left, distance - 1, level + 1)
        GetTopView(root.right, distance + 1, level + 1)
    GetTopView(root, distance, level)
    print('Top View: ', end=' ')
    PrintView(elements)


def PrintView(elements):
    elements_key = [key for key in elements.keys()]
    elements_key.sort()
    [print(elements[key]['value'], end=' ') for key in elements_key]


def LeftView(root):
    if root:
        q = []
        q.append(root)
        while len(q) > 0:
            n = len(q)
            for i in range(1, n + 1):
                temp = q.pop(0)

                if i == 1:
                    print(temp.data, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)


def RightView(root):
    if root:
        q = []
        q.append(root)
        while len(q) > 0:
            n = len(q)
            for i in range(1, n+1):
                temp = q.pop(0)
                if i == 1:
                    print(temp.data, end=' ')
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)


root = Node('A')
root.left = Node('B')
root.right = Node('C')
l_child = root.left
r_child = root.right
l_child.left = Node('D')
l_child.right = Node('E')
r_child.left = Node('F')
r_child.right = Node('G')
l_child.left.left = Node('H')
l_child.left.right = Node('I')
l_child.right.left = Node('J')
BottomView(root, distance=0, level=0)
print()
LeftView(root)
print()
RightView(root)
