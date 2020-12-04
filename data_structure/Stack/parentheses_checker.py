def push(data):
    l.append(data)


def pop():
    l.pop()


top = -1
exp = list(input("enter the expression: "))
l = list()
flag = 1
for i in range(len(exp)):
    if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
        push(exp[i])

    if exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
        if len(l) == 0:
            flag = 0
        else:
            temp = pop()
            if exp[i] == ')' and (temp == '{' or temp == '['):
                flag = 0
            if exp[i] == '}' and (temp == '(' or temp == '['):
                flag = 0
            if exp[i] == ']' and (temp == '(' or temp == '{'):
                flag = 0
if len(l) > 0:
    flag = 0
if flag == 1:
    print("valid expression")
else:
    print("invalid expression")
