# 阶乘，递归
def func1(n):
    if n == 1:
        return 1
    return n * func1(n - 1)
