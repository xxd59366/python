fib = [0,1]
num = int(input('请输入一个数字：'))

for i in range(num-2):
    fib.append(fib[-1] + fib[-2])
    # 前两个数之和，负索引为从右往左
print(fib)