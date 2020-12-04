# infix to postfix
def push(data):
    l.append(data)


def pop():
    t = l.pop()
    return t


exp = list(input("enter the expression"))
l = []
