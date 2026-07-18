def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

for i in range(14):
    print(fib_recursive(i), end=' ')