# stack execution
from stackFunct import Node, Stack

s = Stack()

# enter values to the stack
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.printStack()

# removing values from the stack
s.pop()
s.pop()
s.printStack()

# printing value at top of the stack
print("top is ", s.peek())
