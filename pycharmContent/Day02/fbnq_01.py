fib = [0,1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])
    # 前两个数之和，负索引为从右往左
print(fib)