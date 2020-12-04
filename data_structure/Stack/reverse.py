# reversing a array using stack
from stackFunct import Node, Stack


def reverse(l):
    for i in range(len(l)):
        s.push(l[i])
    for i in range(len(l)):
        l[i] = s.pop()
    return l


s = Stack()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(reverse(l))
