def fib_func(n):
    fib = [0, 1]
    for i in range(n-2):
        fib.append(fib[-2] + fib[-1])
    return fib


n = int(input('长度：'))
print(fib_func(n))
