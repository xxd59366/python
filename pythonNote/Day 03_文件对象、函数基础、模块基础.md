[TOC]



# 一、文件对象

## 1.文件打开方法

### (1) open及file内建函数

+ 作为打开文件之门的"钥匙"，内建函数open()以及file()提供了初始化输入/输出(I/O)操作的通用接口
+ 成功打开文件后会返回一个文件对象，否则引发一个错误
+ open()方法和file()方法可以完全相互替换
+ 基本语法：

```python
file_object = open(file_name,access_mode='r',buffering=-1)
```

### (2) 文件对象访问模式

| 文件模式 | 操作                                       |
| -------- | ------------------------------------------ |
| r        | 以读方式打开(文件不存在则报错)             |
| w        | 以写方式打开(文件存在则清空，不存在则创建) |
| a        | 以追加模式打开(必要时创建新文件)           |
| r+       | 以读写模式打开(参见r)                      |
| w+       | 以读写模式打开(参见w)                      |
| a+       | 以读写模式打开(参见a)                      |
| b        | 以二进制模式打开                           |

## 2.文件输入

### (1) read方法

+ read()方法用来直接读取字节到字符串中，最多读取给定数目个字节

+ 如果没有给定size参数(默认为-1)或者size值为负，文件将被读取直至末尾

```python
>>> f = open('/tmp/mima','w')
>>> f.write('This is mima\n')
13
>>> f.close()
>>> f = open('/tmp/mima','r')
>>> data = f.read()  # 默认读取全部数据
>>> data
'This is mima\n'
>>> data = f.read()  # 因为文件指针已经到文件结尾，再次读取数据为空
>>> data
''
>>> f.close()
```

### (2) readline方法

+ 读取打开文件的一行(读取下个行结束符之前的所有字节)

+ 返回整行内容的字符串(包含行结束符)

+ 也有一个可选的size参数，默认为-1，代表读至行结束符

+ 如果提供了该参数，在超过size个字节后会返回不完整的行

```python
>>> f = open('/tmp/mima')
>>> data = f.readline()
>>> data
'This is mima\n'
```

### (3) readlines方法

+ readlines()方法读取所有(剩余的)行，然后把它们作为一个字符串列表返回

```python
>>> data = f.readlines() # 因为之前已经读到文件末尾，因此data被赋值为一个空列表
>>> data
[]
```

### (4) 文件迭代

+ 如果需要逐行处理文件，可以结合for循环迭代文件

+ 迭代文件的方法与处理其他序列类型的数据类似

+ 最常用的是for循环遍历

```python
>>> f = open('/tmp/test')
>>> for line in f:
...     print(line, end='')
>>> f.close()
```

## 3.文件输出

### (1) write方法

+ write()内建方法功能与read()和readline()相反。它把含有文本数据或二进制数据块的字符串写入到文件中去

+ 写入文件时，不会自动添加行结束标志，需要程序员手工输入

### (2) writelines方法

+ 和readlines()一样，writelines()方法是针对列表的操作

+ 它接受一个字符串列表作为参数，将它们写入文件

+ 行结束字符并不会被自动加入，所以需要的话，必须在调用writelines()前给每行结尾加上行结束符

```python
>>> f = open('/tmp/mima','w')  # 文件不存在则创建，存在则清空文件
>>> f.write('Hello World!\n')
13  # 返回写入到文件的字节数
>>> f.writelines(['2nd line.\n', '3rd line.\n'])
[root@myproxy ~]# cat /tmp/mima  # 此时文件仍然是空的，数据保存在内存中
>>> f.flush()  # 立即将数据从缓存同步到磁盘
[root@myproxy ~]# cat /tmp/mima 
Hello World!
2nd line.
3rd line.
>>> f.write('end\n')
4
>>> f.close()  # 关闭文件时，也会将缓存中数据写入磁盘
[root@myproxy ~]# cat /tmp/mima 
Hello World!
2nd line.
3rd line.
end
```

### (3) 非文本文件

+ 处理非文本文件，与文本文件大体相似，不过在打开文件时，需要使用二进制打开

```python
[root@myproxy ~]# cp /usr/bin/ls /tmp/
>>> f = open('/tmp/ls')
>>> f.read(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.7/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 24: invalid continuation byte
# 报错，因为打开文件时默认以utf-8编码打开，但ls不是文本文件
>>> f = open('/tmp/ls','rb')  # 以bytes类型打开
>>> f.read(10)  # 读取10个字节
b'\x7fELF\x02\x01\x01\x00\x00\x00'
```

## 4.操作文件

### (1) with子句

- 文件打开后如果不关闭，在程序结束时文件自动关闭，但出现内存crash，会丢失数据

+ 使用with语句打开文件，当with语句结束时，文件自动关闭

```python
>>> with open('/tmp/mima') as f:
...     f.readline()
...     f.readline()
... 
'Hello World!\n'
'2nd line.\n'
>>> f.readline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
# 当没有缩进时，文件自动关闭，不能对关闭的文件执行IO操作
```

### (2) 文件内移动

+ seek(x,y)：移动文件指针到不同的位置
  + x是相对于某个位置的偏移量
  + y的值，0表示文件开头，1表示当前位置，2表示文件结尾
  + tell()：返回当前文件指针的位置

```python
[root@myproxy ~]# cat /tmp/mima 
Hello World!
>>> f = open('/tmp/mima')
>>> f.seek(5,0)  # 将指针移动到第五个字节
5
>>> f.read(1)  # 从第5字节位置向后读1个字节，值为Hello World中的空格
' '
>>> f.close()
```

### (3) 标准文件

+ 程序一执行，就可以访问三个标准文件
  + 标准输入：一般是键盘，使用sys.stdin
  + 标准输出：一般是显示器缓冲输出，使用sys.stdout
  + 标准错误：一般是显示器的非缓冲输出，使用sys.stderr

```python
>>> import sys
>>> sys.stdout.write('Hello World!\n')
Hello World!
13
>>> hi = sys.stdin.readline()
hello  
>>> hi
'hello\n'

```

### (4) 案例1：模拟cp操作

> 1. 创建cp.py文件
> 1. 将/bin/ls "拷贝" 到 /root/目录下
> 1. 不要修改原始文件

```python
[root@myproxy Day03]# vim cp.py
# 复制文件
src = open('/bin/ls','rb')
dst = open('/root/ls','wb')
data = src.read()
dst.write(data)
dst.close()
src.close()
# 这样的写法可以实现，但效果不好，如果源文件很大，数据取出来赋值给data，data会消耗大量内存
```

```python
# 每次读4K，减少内存占用
src_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(src_fname, 'rb') as src_f:
    with open(dst_fname, 'wb') as dst_f:
        while True:
            data = src_f.read(4096)
            if not data:
                break
            else:
                dst_f.write(data)
```

```shell
[root@myproxy ~]# ls /bin/ls /tmp/list 
/bin/ls  /tmp/list
[root@myproxy ~]# ^ls^ md5sum
 md5sum /bin/ls /tmp/list 
729c4aa206c5dbc9155c637e932d3716  /bin/ls
729c4aa206c5dbc9155c637e932d3716  /tmp/list
# 将上一条命令中的 ls 改为 md5sum
```

# 二、函数基础

## 1.函数基本操作

### (1) 函数基本概念

- 函数是对程序逻辑进行结构化或过程化的一种编程方法

- 将整块代码巧妙地隔离成易于管理的小块

- 把重复代码放到函数中而不是进行大量的拷贝，这样既能节省空间，也有助于保持一致性

- 通常函数都是用于实现某一种功能

### (2) 创建函数

- 函数使用def语句来创建，语法如下：

```python
def function_name(arguments):
    "function_documentation_string"
    function_body_suite
```

- 标题行由def关键字，函数的名字，以及参数的集合(如果有的话)组成

- def子句的剩余部分包括了一个虽然可选但是强烈推荐的文档字串，和必须的函数体

### (3) 调用函数

+ 通大多数语言相同,python用一堆圆括号调用函数

+ 如果没有加圆括号，只是对函数的引用

```python
def fib_func():
    fib = [0, 1]
    n = int(input('长度: '))
    for i in range(n-2):
        fib.append(fib[-1] + fib[-2])
    print(fib)

fib_func()
```

### (4) 函数的返回值

+ 多数情况下，函数并不直接输出数据，而是向调用者返回值
+ 函数的返回值使用return关键字
+ 没有return的话，函数默认返回None

## 2.函数参数

### (1) 定义参数

- 形式参数
  - 函数定义时，紧跟在函数名后(圆括号内)的参数被称为形式参数，简称形参。由于它不是实际存在的比那里那个，所以又称虚拟变量
- 实际参数
  - 在主调函数中调用一个函数时，函数名后面括弧中的参数(可以是一个表达式)称为"实际参数"，简称实参

### (2) 传递参数

- 调用函数时，实参的个数需要与形参个数一致
- 实参将依次传递给形参

```python
>>> def tfunc(x, y):
...     print('x=%d, y=%d' % (x, y))
... 
>>> tfunc()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tfunc() missing 2 required positional arguments: 'x' and 'y'
>>> tfunc(3, 4)
x=3, y=4
```

### (3) 位置参数

- 与shell脚本类似，程序名以及参数都以位置参数的方式传递给python程序
- 使用sys模块的argv列表接收

```python
import sys
print sys.argv

[root@myproxy Day03]# python3 function_03.py 
['function_03.py']
[root@myproxy Day03]# python3 function_03.py Hello World
['function_03.py', 'Hello', 'World']
```

#### 案例：修改拷贝文件的程序，要求使用函数和位置参数

```python
# 拷贝脚本修改
import sys


def cp_func(src_name, dst_name):
    with open(src_name, 'rb') as src_f:
        with open(dst_name, 'wb') as dst_f:
            while True:
                data = src_f.read(4096)
                if not data:
                    break
                else:
                    dst_f.write(data)


cp_func(sys.argv[1], sys.argv[2])
```

### (4) 默认参数

- 默认参数就是声明了默认值的参数
- 因为给参数赋予了默认值，所以在函数调用时，不向该参数传入值也是允许的

```python
def pstar(num = 20):
    print('*' * num)


pstar()
print()
pstar(40)

[root@myproxy Day03]# python3 function_04.py
********************

****************************************
```

### (5) 参数组

+ 把元组(非关键字参数)或字典(关键字参数)作为参数组传递给函数

+ 定义时：* 表示元组，** 表示字典

+ 调用时：* 表示拆开后面的数据类型，** 表示调用字典

  #### 示例：

  ```python
  def use_mode(name, age):
      print('%s is %s' % (name, age))
  
  
  def fun1(*args):
      print(args)
  
  
  def fun2(**kwargs):
      print(kwargs)
  
  
  def fun3(x, y):
      print(x, y)
  
  
  fun1()
  fun1(10)
  fun1('bob',20)
  fun2()
  fun2(name='bob', age=20)
  fun3(*[10, 5])
  use_mode(**{'name': 'bob', 'age': 25})
  # 输出结果
  ()
  (10,)
  ('bob', 20)
  {}
  {'name': 'bob', 'age': 20}
  10 5
  bob is 25
  ```

  

## 3.函数补充

### (1) 匿名函数

+ lambda
  + lambda可以创造匿名函数，不需要以标注你的def方式来声明
  + 格式：lambda [arg1, arg2, ..., argN]: expression
  + 一个完整的lambda语句就是一个表达式，定义体必须和声明放在同一行
+ filter
  + 调用一个布尔函数来迭代遍历每个序列中的元素; 返回一个使函数返回值为true的元素的序列
  + 格式：filter(function, iterable)
  + 如果布尔函数比较简单，可以直接使用lambda匿名函数代替
+ map
  + 接受一个函数和一个列表，使用函数依次加工列表中的每个元素，得到一个新的列表并返回
  + 格式：map(func, *iterables)

```python
import random

a = lambda x, y: x + y
print(a(3, 4))
alist = [random.randint(1, 100) for i in range(10)]
print(alist)
result = filter(lambda x: x % 2, alist)
# print(result)
# <filter object at 0x0000013E8BB2A5C8>
# 返回的是一个序列，因此要用列表格式显示
print(list(result))
result2 = map(lambda x: x * 2 + 1, alist)
# print(result2)
print(list(result2))
```

### (2) 偏函数

+ 带有多个参数的函数，如果其中某些参数基本上固定的，就可以通过偏函数为这些参数赋默认值
+ 格式：functools.partial(func, *args, **keywords)
+ 示例：

```python
import functools


def foo(a, b, c, d, e):
    return a + b + c + d + e


add = functools.partial(foo, a=1, b=2, c=3, d=4)
add1 = functools.partial(foo, *[1, 2, 3, 4])
add2 = functools.partial(foo, **{'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(add(e=5))
print(add1(5))
print(add2(e=5))
# 以上结果均为15
```

### (3) 递归函数

+ 函数包含了对自身的调用
+ 示例：阶乘

```python
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n -1)


print(factorial(6))
# 输出
720
```

### (4) 生成器(带yield语句的函数)

+ yield语句返回一个值给调用者并暂停执行，next()能从暂停的地方继续执行
+ 当所有的yield语句都被执行后，将不会再有返回
+ 示例：

```python
def mygen():
    yield 'hello'
    a = 10 + 20
    yield a
    yield [1, 2, 3]


for i in mygen():
    print(i)
# 输出
hello
30
[1, 2, 3]
```

### (5) 闭包

+ 函数中嵌套定义另一个函数，内嵌函数引用了外部函数的变量，外部函数返回内嵌函数
+ 用途：保护函数内的变量安全、闭包内的变量和内嵌函数会一直维持在内存中
+ 装饰器：函数调用时用闭包进行装饰
  + 应用情况：
    + 引入日志
    + 增加计时逻辑来检测性能
    + 给函数加入事务的能力
+ 示例1：输出红色字体

```python
def color(func):
    def red(*args):
        return "\033[031;1m%s\033[0m" % func(*args)
    return red


@color
def hello(word):
    return 'hello %s' % word


def welcome():
    return 'welcome'


print(hello('world!'))
print(color(welcome)())
# 输出为红色
hello world!
welcome
```

- 示例2：函数计时器

```python
import time


def count_time(func):
    start_time = time.time()

    def ct(*args):
        func(*args)
        end_time = time.time()
        return end_time - start_time

    return ct


def func1():
    time.sleep(1)


def func2():
    time.sleep(2)


if __name__ == '__main__':
    print(count_time(func1)())
    print(count_time(func2)())
```



# 三、模块基础

## 1.定义模块

### (1) 模块基本概念

- 模块是从逻辑上组织python代码的形式
- 当代码量变得相当大的时候，最好把代码分成一些有组织的代码段，前提是保证它们的彼此交互
- 这些代码片段相互间有一定的联系，可能是一个包含数据成员和方法的类，也有可能是一组相关但彼此独立的操作函数

### (2) 创建模块

- 模块物理层面上组织模块的方法是文件，每一个以.py为结尾的python文件都是一个模块
- 模块名称切记不要与系统中已存在的模块重名
- 模块文件名字去掉后面的扩展名(.py)即为模块名
  - 首字符必须是字母或下划线
  - 其他字符可以是数字、字母、下划线
  - 区分大小写

## 2.使用模块

### (1) 导入模块(import)

- 使用import导入模块
- 模块被导入后，程序会自动生成pyc的字节码文件以提升性能
- 模块属性通过"模块名.属性"的方法调用
- 如果仅需要模块中的某些属性，也可以单独导入

```python
>>> import sys
>>> import os,string
>>> string.digits
'0123456789'
>>> from random import randint
>>> randint(1,10)
3
```

```python
# 自己创建一个模块
'''
小星星

本程序有一个变量hi
还有一个函数pstar
'''
hi = 'Hello World!'
def pstar(n=30):
    "用于打印一行星号"
    print('*' * n)

[root@myproxy Day03]# python3
>>> import module_01  # 将自己写的程序文件当做模块导入
>>> help(module_01)  # 查看帮助信息，观察帮助内容与文件内容
>>> module_01.
module_01.hi      module_01.pstar(  
>>> module_01.hi
'Hello World!'
>>> module_01.pstar()
******************************
>>> module_01.pstar(40)
****************************************
```



### (2) 模块加载(load)

- 一个模块只被加载一次，无论它被导入多少次
- 只加载一次可以阻止多重导入时代码被多次执行
- 如果两个文件相互导入，防止了无限的相互加载
- 模块加载时，顶层代码会自动执行，所以只将函数放入模块的顶层是良好的编程习惯
- 当main直接调用函数时，会直接将函数执行，因此需要加入判断，使模块在被调用时不会自动执行，而在直接运行时执行。

```python
if __name__ == '__main__'
	pstar()
```



### (3) 模块导入的特性

- 模块具有一个"\__name__"特殊属性
- 当模块文件执行时，\__name__的值就是该模块的名字

```python
[root@myproxy Day03]# vim module_test.py
print(__name__)
[root@myproxy Day03]# python3 module_test.py
__main__
[root@myproxy Day03]# vim module_bar.py
[root@myproxy Day03]# cat module_bar.py
import module_test
[root@myproxy Day03]# python3 module_bar.py
module_test
```

### (4) 案例1：生成随机密码

> 创建randpass.py脚本，要求如下：
>
> 1. 编写一个能生成8位随机密码的程序
>
> 2. 使用random的choice函数随机取出字符
>
> 3. 改进程序，用户可以自己决定生成多少位的密码

```python
# 初始版本

# 改进后
import random
import string


def passinit():
    mystr = string.ascii_letters+string.digits
    p=''
    n = int(input('生成密码的位数：'))
    for i in range(n):
        p += random.choice(mystr)

    print('Your pass is %s' % p)


if __name__ == '__main__':
    passinit()
```

