[TOC]

# **一、判断语句**

## 1.if语句

### (1) if语句语法结构

· 标准if条件语句句法

```python
if expression:
    if_suite
else:
    else_suite
```

· 如果表达式的值非0或者为布尔值True，则代码组if_suite被执行; 否则执行else_suite

· 代码组是一个python属于，它由一条或多条语句组成，表示一个子代码块

### (2) if语句示例解析

· 只要表达式数字为非零值即为True

```python
>>> if 10:
...     print('Yes')
... 
Yes
>>> if 0:
...     print('Yes')
... else:
...     print('No')
... 
No
# 数据类型也可以作为判断条件，任何值为0的数字都是False，非0为True
# 其他非空对象为True，空对象为False
# None也表示False
```

### (3) 案例1：判断合法用户

> 1. 创建login2.py文件
> 1. 提示用户输入用户名和密码
> 1. 得到相关信息后，将其保存在变量中
> 1. 如果用户输的用户名为bob，密码为123456则输出Login successful，否则输出Login inorrect

```python
import getpass
print('-' * 20 + '请输入用户名和密码' + '-' * 20)
uname = input('用户名：')
# getpass模块隐藏在终端输入的密码
passwd = getpass.getpass('密码：')
if uname.__eq__('bob') and passwd.__eq__('123456'):
    print('Login successful')
else:
    print('Login incorrect')
```

· 验证时需要在终端中打开，而非在pycharm中直接run

## 2.扩展if语句

### (1) 扩展if语句结构

```python
if expression1:
    if_suite
elif expression2:
    elif_suite
else:
    else_suite
```

### (2) 条件表达式

· python在很长一段时间里没有条件表达式(C?X:Y)，条件表达式又称三元运算符，范·罗萨姆一直拒绝加入这样的功能

· 从python 2.5集成的语法确定为：X if C else Y

```shell
>>> x, y = 3, 4
>>> small = x if x < y else y
>>> print small
3
```

### (3) 案例1：编写判断成绩的程序

> 创建grade.py脚本，根据用户输入的成绩分档，要求如下：
>
> 1. 输入成绩需为0-100之间的数
> 1. 成绩大于60分，输出"及格"
> 1. 成绩大于70分，输出"良好"
> 1. 成绩大于80分，输出"好"
> 1. 成绩大于90分，输出"优秀"
> 1. 否则输出"你要努力了"

```python
print('-' * 20 + '请输入考试成绩' + '-' * 20)
grade = int(input())
if grade >= 0 and grade <=100:
    if grade >= 90:
        print('优秀')
    elif grade >= 80:
        print('好')
    elif grade >= 70:
        print('良好')
    elif grade >= 60:
        print('及格')
    else:
        print('你要努力了！')
else:
    print('错误，输入不合法！请输入0-100！')
```

### (4) 案例2：编写石头剪刀布的小游戏

> 编写game.py，要求如下：
>
> 1. 计算机随机出拳
> 1. 玩家自己决定如何出拳
> 1. 代码尽量简化

tips：random.choice：从字符串中任选一个字符，从列表中任选一个元素

```python
>>> import random
>>> random.choice('abc')
'a'
>>> random.choice('abc')
'c'
>>> random.choice(['aaa', 'bbb', 'ccc'])
'ccc'
>>> random.choice(['aaa', 'bbb', 'ccc'])
'bbb'
```

· 代码部分

```python
import random
print('-' * 20 + '这是一个猜拳游戏' + '-' * 20)
all_choices = ['石头', '剪刀', '布']
robot = random.choice(all_choices)
# 将石头剪刀布的值转化为数字(转化为索引下标)
############
prompt = '''(0) 石头
(1)剪刀
(2) 布
请选择(0/1/2)'''
index = int(input(prompt))
player = all_choices[index]
############

player = input('石头/剪刀/布：')
win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]

if player in all_choices:
    print('电脑出的是 %s' % (robot))
#   print('电脑出的是', robot)
# 要养成使用占位符的习惯
    if player.__eq__(robot):
        print('平局！')
    elif [player, robot] in win_list:
        print('\033[32;1m你赢了！\033[0m')
# 显示为绿色
    else:
        print('\033[31;1m你输了！\033[0m')
# 显示为红色
else:
    print('输入不合法！')
```

# **二、while循环**

## 1.循环语句基础

### (1) 循环概述

· 一组被重复执行的语句称之为循环体，能否继续重复，决定循环的终止条件

· python中的循环有while循环和for循环

· 循环次数未知的情况下，建议采用while循环

· 循环次数可以预知的情况下，建议采用for循环

### (2) while循环语法结构

· 当需要语句不断地重复执行时，可以使用while循环

```python
while expression:
    while_suite
```

· 语句while_suite会被连续不断地循环执行，直到表达式的值变成0或False

```python
sum100 = 0
counter = 1

while counter <= 100:
    sum100 += counter
    counter += 1
print ('result is %d' % sum100)
```

- 猜数字游戏

```python
import random

# 随机取出100以内的整数，包括1和100
num = random.randint(1, 100)
prompt = "'-' * 20 + '猜数字游戏' + '-' * 20"

while True:
    x = input('请输入1-100的数字:\n')
    if x == '':
        prompt = '请输入！'
        print(prompt)
    else:
        gamer = int(x)
        if 1 <= gamer <= 100:
            if gamer == num:
                prompt = '恭喜猜对了!'
                print(prompt)
                break
            else:
                prompt = '猜大了！' if gamer > num else '猜小了'
                print(prompt)
        else:
            prompt = '输入不合法!'
            print(prompt)
```



## 2.循环语句进阶

### (1) break语句

· break语句可以结束当前循环然后跳转到下条语句

· 写程序的时候，应尽量避免使用重复的代码，在这种情况下可以使用wihile-break结构

```python
name = input('uname:')
while name != 'tom':
    name = input('uname:')
# 可以替换为
while True:
    name = input('uname:')
    if name == 'tom':
        break
```

### (2) continue语句

· 当遇到continue语句时，程序会终止当前循环，并忽略剩余的语句，然后回到循环的顶端

· 如果仍然满足循环条件，循环体内语句继续执行，否则退出循环

```python
sum100 = 0
counter = 0
while counter <= 100:
    counter += 1
    if counter % 2:
        countinue
    sum100 += counter
print("result is %d" % sum100)
```

### (3) else语句

· python中的while语句也支持else子句

· else子句只在循环完成后执行

· break语句也会跳过else块

```python
sum10 = 0
i = 1
while i <= 10:
    sum10 += i
    i += 1
else:
    print(sum10)
```

### (4) 案例1：完善石头剪刀布小游戏

> 编写game_02.py，要求如下：
>
> 1. 基于上节game.py程序
> 1. 实现循环结构，要求游戏三局两胜

```python
import random
print('-' * 20 + '这是一个猜拳游戏' + '-' * 20)
result = {'pwin': 0, 'rwin': 0}
while result['pwin'] < 2 and result['rwin'] < 2:
    all_choices = ['石头', '剪刀', '布']
    robot = random.choice(all_choices)
    prompt = '''(0) 石头
(1)剪刀
(2) 布
请选择(0/1/2)'''
    index = int(input(prompt))
    player = all_choices[index]
    win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]

    if player in all_choices:
        print('电脑出的是 %s' % (robot))
        if player.__eq__(robot):
            print('平局！')
        elif [player, robot] in win_list:
            print('\033[32;1m你赢了！\033[0m')
            result['pwin'] += 1
        else:
            print('\033[31;1m你输了！\033[0m')
            result['rwin'] += 1
    else:
        print('输入不合法！')
    print('比分为 \033[31;1m%s : %s\033[0m' % (result['pwin'], result['rwin']))
print('\033[31;1m游戏结束！\033[0m')
```



### (5) 猜数程序

> 编写guess.py，要求如下：
>
> 1. 系统随机生成100以内数字
> 1. 要求用户猜生成的数字是多少
> 1. 最多猜5次，猜对结束程序
> 1. 如果5次全部猜错，则输出正确结果

```python
import random

# 随机取出100以内的整数，包括1和100
num = random.randint(1, 100)
prompt = "'-' * 20 + '猜数字游戏' + '-' * 20"
counter = 0

while counter < 5:
    x = input('请输入1-100的数字:\n')
    if x == '':
        prompt = '请输入！'
        print(prompt)
    else:
        gamer = int(x)
        if 1 <= gamer <= 100:
            if gamer == num:
                prompt = '恭喜猜对了!'
                print(prompt)
                break
            else:
                counter += 1
                prompt = '猜大了！' if gamer > num else '猜小了'
                print(prompt)
        else:
            prompt = '输入不合法!'
            print(prompt)
else:
    print('正确值为 %s' % num)
    
# 使用while的else格式，只有在break不触发时，else才会执行
```



# **三、for循环**

## 1.for循环详解

### (1) for循环语法结构

· python中的for接受可迭代对象(序列或迭代器)作为参数，每次迭代其中一个元素

```python
for iter_var in iterable:
    suite_to_repeat
```

· 与while循环一样，支持break、continue、else语句

· 一般情况下，循环次数未知采用while循环，循环次数已知，采用for循环

### (2) range函数

· for循环常与range函数一起使用

· range函数提供循环条件

· range函数的完整语法为：

```python
range(start, end, step=1)
```

· range函数只给一个数字作为参数，表示结束数字(不包含)，起始数字默认是0

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in range(1, 11, 2):
...     print(i)
... 
1
3
5
7
9
>>> for i in range(10, 0, -1):
...     print(i)
... 
10
9
8
7
6
5
4
3
2
1
astr = 'python'
alist = [10, 20, 30]
atuple = ('tom', 'jerry')
adict = {'name': 'bob', 'age': 20}

for ch in astr:
    print(ch)
for i in alist:
    print(i)
for name in atuple:
    print(name)
for key in adict:
    print('%s %s' % (key,adict[key]))
```



### (3) 列表解析

· 它是一个非常有用、简单、而且灵活的工具，可以用来动态地创建列表

· 语法：

```python
[expr for iter_var in iterable]
```

· 这个语句的核心是for循环，它迭代iterable对象的所有条目

· expr应用于序列的每个成员，最后的结果值是该表达式产生的列表

```python
>>> [5]
[5]
>>> [5 + 2]
[7]
>>> [5 + 2 for i in range(10)]
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
>>> [5 + i for i in range(1,11)]
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```



### (4) 案例1：斐波那契数列

> 1. 斐波那契数列就是某一个数，总是前两个数之和，如，0, 1, 1, 2, 3, 5, 8
> 1. 使用for循环和range函数编写一个程序，计算有10个数字的斐波那契数列
> 1. 改进程序，要求用户输入一个数字，可以生成用户需要的长度的斐波那契数列

```python
fib = [0,1]
num = int(input('请输入一个数字：'))

for i in range(num-2):
    fib.append(fib[-1] + fib[-2])
    # 前两个数之和，负索引为从右往左
print(fib)
```

### (5) 案例2：九九乘法表

> 1. 创建mtable.py程序
> 1. 程序运行后，可以在屏幕上打印出99乘法表
> 1. 修改程序，由用户输入数字，可打印出任意数字的乘法表

```python
# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        endch = '\n' if i == j else '\t'
        print('%s*%s=%s' % (j, i, i*j), end=endch)
        
# 自定义乘法表
num = int(input('XX乘法表?\n'))
for i in range(1,num+1):
    for j in range(1,i+1):
        endch = '\n' if i == j else '\t'
        print('%s*%s=%s' % (j, i, i*j), end=endch)
```

### (6) 案例3：列表解析

> 通过列表解析生成192.168.1.1-192.168.1.254

```python
>>> ips = [ "192.168.1."+str(i) for i in range(1,255) ]
>>> ips = ['192.168.1.%s' % i for i in range(1,255)]
```



