[TOC]

# 一、函数基础

## 1.创建函数

### (1) def语句

- 函数用def语句创建，语法如下：

```python
def function_name(arguments):
    "function_documentation_string"
    function_body_suite
```

- 标题行由def关键字，函数的名字，以及参数的集合(如果有的话)组成
- def子句的剩余部分包括了一个虽然可选但是强烈推荐的文档字串，和必须的函数体

### (2) 前向引用

- 函数不允许在函数未声明之前对其进行引用或者调用

```python
def foo():
    print('in foo')
    bar()
foo()  # 报错，因为bar没有定义
```

```python
def foo():
    print('in foo')
    bar()
def bar():
    print('in bar') 
foo()  # 正常执行
```

### (3) 内部函数

- 在函数体内创建另外一个函数是完全合法的，这种函数叫做内部函数/内嵌函数

```python
>>> def foo():
...     def bar():
...         print('bar() is called')
...     print('foo() is called')
...     bar()
...     
>>> foo()
foo() is called
bar() is called
>>> bar()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'bar' is not defined
```

## 2.调用函数

### (1) 函数操作符

+ 使用一对圆括号()调用函数，如果没有圆括号，只是对函数的引用
+ 任何输入的参数都必须放置在括号中

```python
>>> def foo():
...     print('hello world')
...     
>>> foo()
hello world
>>> foo
<function foo at 0x000002CC83E960D8>
```

### (2) 关键字参数

- 关键字参数的概念仅仅针对函数的调用
- 这种理念是让调用者通过函数调用中的参数名字来区分参数
- 这样规范允许参数缺失或者不按顺序

```python
>>> def get_info(name, age):
...     print('%s is %s years old.' % (name, age))
...      
>>> get_info('bob', 20)
bob is 20 years old.
>>> get_info(20, 'bob')
20 is bob years old.
# 关键字参数
>>> get_info(age=20, 'bob')  # Error，关键字参数必须在后
>>> get_info(20, name='bob')  # Error，name得到了多个值
>>> get_info('bob', 20, 100)  # Error，参数过多
>>> get_info(age=20, name='bob')
bob is 20 years old.
```

### (3) 参数组

- python允许程序员执行一个没有显式定义参数的函数
- 相应的方法是通过一个把元组(非关键字参数，用*表示)或字典(关键字参数，用**表示)作为参数组传递给函数
- 传参时加上*或**表示把序列或字典拆开

```python
# 参数组
>>> def func01(*args):
...     print(args)
...     
>>> func01('tom')
('tom',)
>>> func01('tom', 20)
('tom', 20)
>>> def func02(**args):
...     print(args)
...     
>>> func02(name='bob',age=20)
{'name': 'bob', 'age': 20}
# 拆分序列
>>> def add(a, b):
...     return a + b
... 
>>> nums = [10, 20]
>>> add(nums)  # 报错，nums只传给了a，b没有进行赋值
>>> add(*nums)  # 将序列拆分后分别赋值给a和b
30
```

### (4) 案例：简单的加减法数学游戏

> 1. 随机生成两个100以内的数字
> 1. 随机选择加法或是减法
> 1. 总是使用打的数字减去小的数字
> 1. 如果用户答错三次，程序给出正确的答案

```python
import random


def num_ac():
    num = [random.randint(1, 100) for i in range(2)]
    return num


def num_todo():
    num = num_ac()
    wtdo = random.randint(1, 2)
    if wtdo == 1:
        result = num[0] + num[1]
    else:
        result = max(num[0], num[1]) - min(num[0], num[1])
    return num, result


def show_menu():
    num, result = num_todo()
    prompt = """The numbers are %s and %s,
input the result: """ % (num[0], num[1])
    count = 0

    while True:
        count += 1
        guess = int(input(prompt))
        if guess == result:
            print('you are right ~~^_^~~')
            break

        if count == 3:
            print('Your chance has used up.The result is %s' % result)
            break

        print('Not right. try again please. You have %s chance yet.' % (3-count))
        continue


if __name__ == '__main__':
    show_menu()
```



## 3.匿名函数

### (1) lambda

- python允许用lambda关键字创造匿名函数
- 匿名是因为不需要以标准的def方式来声明
- 一个完整的lambda语句代表了一个表达式，这个表达式的定义体必须和声明放在同一行

```python
lambda [arg1[, arg2, ..., argN]]:expression
```

### (2) filter()函数

- 用于过滤数据
- filter(func, seq)：调用一个布尔函数func来迭代遍历每个序列中的元素; 返回一个使func返回值为true的元素序列
- 如果布尔函数比较简单，直接使用lambda匿名函数就显得非常方便

```python
>>> from random import randint
>>> nums = [randint(1, 100) for i in range(10)]
>>> nums
[88, 20, 21, 32, 33, 32, 84, 60, 58, 84]
>>> def func1(x):
...     return True if x % 2 == 0 else False
>>> list(filter(func1, nums))
[88, 20, 32, 32, 84, 60, 58, 84]  # 筛选出所有的偶数(即过滤奇数)

>>> list(filter(lambda x: True if x % 2 == 0 else False, nums))
[88, 20, 32, 32, 84, 60, 58, 84]
```

### (3) map()函数

- 用于加工数据
- map(func, seq)，将seq中的每一项作为func的参数，func将数据加工处理后返回。

```python
>>> from random import randint
>>> nums = [randint(1, 100) for i in range(10)]
>>> def func2(x):
...     return x * 2
... 
>>> list(map(func2, nums))
[32, 14, 152, 72, 146, 160, 188, 56, 192, 66]
>>> nums
[16, 7, 76, 36, 73, 80, 94, 28, 96, 33]
```



# 二、函数高级应用

## 1.变量作用域

### (1) 全局变量

- 标识符的作用域是定义为其声明在程序里的可应用范围，也就是变量的可见性
- 在一个模块中最高级别的变量有全局作用域
- 在一个模块中最高级别的变量有全局作用域
- 全局变量的一个特征是除非被删除掉，否则他们的存活到脚本运行结束，且对于所有的函数，他们的值都是可以被访问的

```python
>>> def func2():
...     y=100
...     print(y)
...     
>>> func2()
100
>>> print(y)  # NameError，局部变量不能在全局使用
```

### (2) 局部变量

- 局部变量只是暂时地存在，仅仅只依赖于定义它们的函数现阶段是否处于活动
- 当一个函数调用出现时，其局部变量就进入声明它们的作用域，在那一刻，一个新的局部变量名为此对象创建
- 一旦函数完成，框架被释放，变量将会离开作用域

```python
>>> def func3():
...     x = 'hello world'
...     print(x)
...     
>>> func3()
hello world
>>> print(x)
10
```

### (3) global语句

- 因为全局变量的名字能被局部变量给遮盖掉，所以为了明确地引用一个已命名的全局变量，必须使用global语句

```python
>>> x = 4
>>> def func4():
...     global x
...     x = 10
...     print(x)
...     
>>> func4()
10
>>> print(x)
10
```

### (4) 名字空间

- 任何时候，总有一个到三个活动的作用域(内建、全局和局部)
- 标识符的搜索顺序依次是局部、全局和内建
- 提到名字空间，可以想象是否有这个标识符
- 提到变量作用域，可以想象是否可以"看见"这个标识符

```python
>>> def func5():
...     x = 'hello'
...     print(len(x))
...     
>>> func5()
5
>>> len=100
>>> func5()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 3, in func5
TypeError: 'int' object is not callable
```

## 2.函数式编程

### (1) 偏函数

- 偏函数的概念是将函数式编程的概念和默认参数以及可变参数结合在一起
- 一个带有多个参数的函数，如果其中某些参数基本上固定，那么就可以通过偏函数为这些参数赋默认值

```python
# int函数默认将字符类型的数字转换成10进制整数
>>> int('1010', base=2)  # 通过base=2将1010标记为二进制数
10  # 输出为10进制数
>>> int('1010')
1010
# 改造int函数，使其不需要多次声明base=2
>>> from functools import partial
>>> int2 = partial(int, base=2)
>>> int2('1010')
10

# 改造add函数，固定前4个值
>>> def add(a, b, c, d, e):
...     return a + b+ c + d + e
... 
>>> add(10,20,30,40,1)
101
>>> add(10,20,30,40,2)
102
>>> add100 = partial(add,10,20,30,40)  # 依次赋值，固定前4个参数值
>>> add100(5)
105
```

### (2) 递归函数

- 如果函数内部包含了对自身的调用，该函数就是递归的
- 在操作系统中，查看某一目录内所有文件、修改权限等都是递归的应用

```python
def func1():
    if x == 1:
        return x
    return x * func1(x - 1)
```

#### 案例：快速排序

> 1. 随机生成10个数字
> 1. 利用递归，实现快速排序

- 思路：
  - 假设第一个数是中间值，赋值给middle
  - 遍历剩余的数字，比middle小的放到smaller列表，比middle大的放到lager列表
  - 把smaller，middle，larger拼接起来
  - smaller和larger继续使用相同方法进行排序

```python
import random


def kp(seq):
    if len(seq) < 2:
        return seq
    middle = seq[0]
    smaller = []
    larger = []

    for num in seq[1:]:
        if num <= middle:
            smaller.append(num)
        else:
            larger.append(num)

    return kp(smaller) + [middle] + kp(larger)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    print(nums)
    result = kp(nums)
    print(result)
```

### (3) 生成器

- 从句法上讲，生成器是一个带yield语句的函数
- 一个函数或者子程序只返回一次，但一个生成器能暂停执行并返回一个中间的结果
- yield语句返回一个值给调用者并暂停执行
- 当生成器的next()方法被调用的时候，它会准确地从离开的地方继续
- 与迭代器相似，生成器以另外的方式来运作
- 当到达一个真正的返回或者函数结束没有更多的值返回，StopIteration异常就会被抛出

- 生成器对象

```python
# 生成一个大列表
>>> ['192.168.1.%s' % i for i in range(1, 255)]
# 生成一个生成器对象
>>> ('192.168.1.%s' % i for i in range(1, 255))
<generator object <genexpr> at 0x000001DDEA60C348>
# 调用生成器对象
>>> ips = ('192.168.1.%s' % i for i in range(1, 255))
>>> for ip in ips:
...     print(ip)
```

- 函数的形式
  - 与普通的函数有所区别。一般来说，函数通过return返回一个值，生成器函数可以通过yield关键字返回很多中间结果

```python
>>> def mygen():
...     yield 100
...     a = 10 + 20
...     yield a
...     yield 300
...     
>>> mg = mygen()
>>> mg
<generator object mygen at 0x000001DDEA605BC8>
>>> for i in mg:
...     print(i)
...     
100
30
300
```

### (4) 模块

- 导入模块时，python将会到sys.path定义的路径下查找模块，如果查到则导入，否则报错

```python
>>> import sys
>>> sys.path
['D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\pydev', 'G:\\python\\pycharmContent', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\third_party\\thriftpy', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\pydev', 'D:\\pythonWinENV\\python-3.7.4-full\\python37.zip', 'D:\\pythonWinENV\\python-3.7.4-full\\DLLs', 'D:\\pythonWinENV\\python-3.7.4-full\\lib', 'D:\\pythonWinENV\\python-3.7.4-full', 'D:\\pythonWinENV\\python-3.7.4-full\\lib\\site-packages', 'G:\\python\\pycharmContent', 'G:/python/pycharmContent']
```



## 3.内部模块

### (1) hashlib模块

- 用于计算文件的哈希值：md5/sha/sha256/sha512

```python
# 通过hashlib计算md5值
>>> import hashlib
>>> m = hashlib.md5(b'123456')
>>> print(m)
<md5 HASH object @ 0x000001DDEA5DD4B0>
>>> m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'

# 计算文件的md5值
>>> import hashlib
>>> with open('/etc/passwd', 'rb'):
...     data = 
KeyboardInterrupt
>>> with open('/etc/passwd', 'rb') as f:
...     data = f.read()
... 
>>> m = hashlib.md5(data)
>>> m.hexdigest()
'ee7fea30750df626c3bed957e1a41d27'

# 分批读入内容，多次更新计算
>>> m1 = hashlib.md5()
>>> m1.update(b'12')
>>> m1.update(b'34')
>>> m1.update(b'56')
>>> m1.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'
```

#### 案例：计算文件的md5值

> 1. 通过命令行的位置参数给定文件名
> 1. 计算出文件的md5值并打印到屏幕上

```python
import sys
import hashlib


def md5check(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)

        result = m.hexdigest()

    return result


if __name__ == '__main__':
    fname = sys.argv[1]
    result = md5check(fname)
    print(result)
```



### (2) tarfile模块

- tarfile模块允许创建、访问tar文件，实现打包、压缩
- 同时支持gzip、bzip2格式

```python
# 压缩操作
>>> import tarfile
>>> tar = tarfile.open('G:\python\pycharmContent\Day07\mytest.tar.gz', 'w:gz')  # 用gizp压缩
>>> tar.add('G:\python\pycharmContent\Day07\jc_01.py')  # 压缩单个文件
>>> tar.add(r'G:\python\pycharmContent\tmp')  # 压缩目录
>>> tar.close()  # 关闭

# 解压操作
>>> tar = tarfile.open('G:\python\pycharmContent\Day07\mytest.tar.gz')
>>> tar.extractall(r'G:\python\pycharmContent\Day07\tmp')
>>> tar.close()
```

#### 案例：备份程序

> 1. 需要支持完全和增量备份
> 1. 周一执行完全备份
> 1. 其他时间执行增量备份
> 1. 备份文件需要打包为tar问阿金并使用gzip格式压缩

- 思路：
  - 判断文件是否变化：md5
  - 完全备份需要执行备份目录、计算每个文件的md5值
  - 增量备份需要计算文件的md5值，与前一天的MD5比较，有变化则备份; 目录中新增的文件也需要备份
  - 备份文件名应该体现出备份的是哪个目录，是增量还是完全，是哪一天备份的