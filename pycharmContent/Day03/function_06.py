import random

a = lambda x, y: x + y
print(a(3, 4))
alist = [random.randint(1, 100) for i in range(10)]
print(alist)
result = filter(lambda x: x % 2, alist)
print(result)
# 返回的是一个序列，因此要用列表格式显示
print(list(result))
result2 = map(lambda x: x * 2 + 1, alist)
print(result2)
print(list(result2))
