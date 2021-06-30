# using recursion
print('using recursion')


def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibo(7))


# using dp
print('using dp')


def fibonacci(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


n = 50
memo = [-1 for i in range(n+1)]
print(fibonacci(n, memo))
