# postfix calculations
def push(data):
    l.append(data)


def pop():
    t = l.pop()
    return t


exp = list(input("enter the expression: "))
l = []

for i in range(len(exp)):
    if exp[i].isdigit():
        push(int(exp[i]))
    elif exp[i] == "+":
        n = pop()
        m = pop()
        sum = m + n
        push(sum)
    elif exp[i] == "-":
        n = pop()
        m = pop()
        sum = m - n
        push(sum)
    elif exp[i] == "*":
        n = pop()
        m = pop()
        sum = m * n
        push(sum)
    elif exp[i] == "/":
        n = pop()
        m = pop()
        sum = m / n
        push(sum)
print(pop())
