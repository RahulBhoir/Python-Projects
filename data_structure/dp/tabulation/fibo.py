# method one
def fibo(n):
    table = [0 for i in range(n + 1)]
    table[1] = 1
    for i in range(n+1):
        if i == n - 1:
            table[i+1] += table[i]
            break
        else:
            table[i+1] += table[i]
            table[i+2] += table[i]
    print(table[n])


fibo(50)

# method two
# TC = O(n)
# SC = O(n)
n = 50
a = []
a.append(0)
a.append(1)
for i in range(2, n+1):
    a.append(a[i-1] + a[i - 2])
print(a[50])
