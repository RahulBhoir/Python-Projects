n = 5
for i in range(1, n+1):
    for j in range(i, n+1):
        print(j, end=' ')
    print()


for i in range(n):
    for j in range(n-i):
        print(j, end=' ')
    print()


for i in range(1, n):
    for j in range(1, n - i + 2):
        print(j % 2, end=' ')
    print()

for i in range(1, n+1):
    for j in range(i):
        print("*", end=' ')
    print()

for i in range(1, n+1):
    for space in range(i, 15):
        print(' ', end=' ')
    for j in range(1, i+1):
        print('* ', end=' ')
    print()
