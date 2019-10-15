[TOC]

# 1.系统管理模块

## 1.shutil模块

### (1) 复制和移动

- shutil.copyfilebj(fsrc, fdst[, length])
  - 将类似文件的对象fsrc的内容复制到类似文件的对象fdst
- shutil.copyfile(src, dst, *, follow_symlinks=True)
  - 将名为src的文件的内容(无元数据)复制到名为dst的文件，然后返回dst
- shutil.copy(src, dst, *, follow_symlinks=True)
  - 将文件src复制到文件或目录dst，src和dst应为字符串，如果dst指定目录。则文件将使用src的基本文件名复制到dst中，返回新创建的文件的路径。
- shutil.copy2(src, dst, *, follow_symlinks=True)
  - 与copy()相同，但copy2()也尝试保留所有文件元数据，等同"cp -p"
- shutil.move(src, dst, copy_function=copy2)
  - 递归地将文件或目录(src)移动到另一个位置(dst)，并返回目标

### (2) 目录操作

- shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
  - 递归地复制以src为根的整个目录树，返回目标目录。由dst命名的目标目录不能已经存在
- shutil.rmtree(path, ignore_errors=False, onerror=None)
  - 删除整个目录树; 路径必须指向目录(而不是指向目录的符号链接)

### (3) 权限管理

- shutil.copymode(src, dst, *, follow_symlinks=True)
  - 将权限位从src复制到dst。文件内容、所有者和组不受影响。src和dst是以字符串形式给出的路径和名称。
- shutil.copystat(src, dst, *, follow_symlinks=True)
  - 将权限位、最后访问时间、上次修改时间和标志从src复制到dst
- shutil.chown(path, user=None, group=None)
  - 更改给定路径的所有者**用户**和/或**组**

### (4) 案例

```python
import shutil
import os  # 删除单个文件需要导入 os 模块


def cpfobj(src, dst):
    # copyfile值了解底层原理，实际代码不需要使用
    f1 = open(src, 'rb')
    f2 = open(dst, 'wb')
    shutil.copyfileobj(f1, f2)
    f1.close()
    f2.close()


def cpf(src, dst):
    # 只拷贝内容
    shutil.copyfile(src, dst)


def cp(src, dst):
    # 既拷贝内容，又拷贝权限
    shutil.copy(src, dst)


def cp2(src, dst):
    # 相当于cp -p
    shutil.copy2(src, dst)


def mv(src, dst):
    # 相当于mv
    shutil.move(src, dst)


def cptr(src, dst):
    # 需要将目标名也写出来
    shutil.copytree(src, dst)


def rmtr(path):
    # 相当于rm -rf，但只能删除目录
    shutil.rmtree(path)


def rm(path):
    # 删除单个文件
    os.remove(path)


if __name__ == '__main__':
    cpfobj('/bin/ls', '/tmp/list5')
    cpf('/bin/ls', '/tmp/list6')
    cp('/bin/ls', '/tmp/list7')
    cp2('/bin/ls', '/tmp/list8')
    mv('/tmp/list8', '/tmp/list')
    cptr('/etc/security', '/tmp/security')
    mv('/tmp/security', '/var/tmp/auquan')
    rmtr('/var/tmp/auquan')
    rm('/tmp/list5')
```

### (6) python官方手册

https://docs.python.org

## 2.subprocess模块

### (1) 概述

- subprocess模块主要用于调用和执行系统命令
- subprocess模块允许你产生新的进程，连接到它们的输入/输出/错误管道，并获得它们的返回代码
- 本模块旨在替换几个较早的模块和功能，如os.system、os.spawn*

```python
import subprocess
import sys


def subr(com, args):
    for i in args:
        print('\033[031;1m%s %s\033[0m' % (com, i))
        subprocess.run(com+' '+i, shell=True)


if __name__ == '__main__':
    print(sys.argv)
    com = sys.argv[1]
    for i in range(2):
        sys.argv.remove(sys.argv[0])
    args = sys.argv
    # print(args)
    subr(com, args)
    
# subprocess.run的返回值(returncode)为系统的$?
```

```python
# 捕获输出
import subprocess

rc = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(rc.returncode)
print(rc.stdout.decode(), end='')
print(rc.stderr.decode(), end='')
```

# 2.语法风格及布局

### (1) 变量赋值

+ python支持链式多重赋值

```python
x = y = 10
```

+ 另一种将多个变量同时复制的方法称为多元赋值，采用这种方式赋值时，等号两边的对象都是元组

```python
a, b = 10, 20
a, b = b, a  # a 和 b 的值互换
```

### (2) 合法标识符

+ python标识字符串规则和其他大部分用C编写的高级语言相似
+ 第一个字符必须是字母或下划线(_)
+ 剩下的字符可以是字母和数字或下划线
+ 大小写敏感

### (3) 关键字

+ 和其他的高级语言一样，python也拥有一些被称作关键字的保留字符
+ 任何语言的关键字应该保持相对稳定，但因为python是一门不断成长和进化的语言，其关键字偶尔会更新
+ 关键字列表和iskeyword()函数都放入了keyword模块以便查阅

```python
# python关键字
import keyword
keyword.kwlist
keyword.iskeyword('pass')
```

### (4) 内建函数

+ 除了关键字以外，python还有可以在任何一级代码使用的"内建"的名字集合，这些名字可以由解释器设置或使用
+ 虽然built-in不是关键字，但应该把它当做"系统保留字"
+ 保留的常量如：True、False、None

### (5) 模块结构及布局

```python
#!/usr/local/bin/python3
"""
文档字符串，用于帮助
"""
import os  # 导入模块
import time
import string

debug = True  # 全局变量
all_chs = string.ascii_letters + string.digits

class MyClass:  # 类的声明
    pass

def my_func():  # 函数声明
    pass

if __name__ == '__main__':  # 程序主题代码
    mc = MyClass()
    mf = my_func()
```

### (6) 案例：创建文件

> 1. 编写一个程序，要求用户输入文件名
> 1. 如果文件已存在，要求用户重新输入
> 1. 提示用户输入数据，每行数据先写到列表中
> 1. 将列表数据写入到用户输入的文件名中

#### 步骤：

1. 思考：程序运行方式：交互？非交互？

```python
# filename: /etc/hosts
文件已存在，请重试
# filename: /tmp/abc.txt
请输入内容，输入end表示结束
(end to quit)> Hello World!
(end to quit)> the end.
(end to quit)> byebye.
(end to quit)> end
```

2. 分析程序有哪些功能，将功能写成函数，编写出大致框架

```python
def get_fname():
    '用于获取文件名'
    pass

def get_content():
    '用于获取文件内容'
    pass

def wfile(fname, content):
    '将内容写入文件'
    pass
```

3. 编写程序主体，依次调用各个函数

```python
if __name__ == '__main__':
    get_fname()
    get_content()
    wfile(fname, content)
```

4. 程序：

```python
import os


def get_fname():
    """用于获取文件名"""
    while True:
        fname = input('请输入文件名：')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')
    return fname


def get_content():
    """用于获取文件内容"""
    content = []
    print('请输入内容，end表示结束')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        line += '\n'
        content.append(line)
    return content


def wfile(fname, content):
    """将内容写入文件"""
    with open(fname, 'w') as f:
        f.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
```

# 3.字符串详解

## 1.序列

### (1) 序列类型操作符

| 序列操作符     | 作用                             |
| -------------- | -------------------------------- |
| seq[ind]       | 获得下标为ind的元素              |
| seq[ind1:ind2] | 获得下标从ind1到ind2间的元素集合 |
| seq * expr     | 序列重复expr次                   |
| seq1 + seq2    | 连接序列seq1和seq2               |
| obj in seq     | 判断obj元素是否包含在seq中       |
| obj not in seq | 判断obj元素是否不包含在seq中     |



### (2) 内建函数

| 函数        | 含义                               |
| ----------- | ---------------------------------- |
| list(iter)  | 把可迭代对象转换为列表             |
| str(obj)    | 把obj对象转换成字符串              |
| tuple(iter) | 把一个可迭代对象转换成一个元组对象 |

```python
# list用于转换成列表
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list(range(5))
[0, 1, 2, 3, 4]

# str用于转成字符串
>>> str(100)
'100'

# tuple用于转换成元组
>>> tuple(['tom','jerry','minister'])
('tom', 'jerry', 'minister')
```

- len(seq)：返回seq长度
- enumerate：接受一个可迭代对象作为参数，返回一个enumerate对象
- max(iter, key=None)：返回iter中的最大值
- reversed(seq)：接受一个序列作为参数，返回一个以逆序访问的迭代器
- sorted(iter)：接受一个可迭代对象作为参数，返回一个有序的列表

- 常用于序列对象的方法：

```python
>>> from random import randint
>>> num_list = [randint(1, 100) for i in range(5)]
>>> num_list
[65, 36, 6, 6, 18]
# reversed用于翻转
>>> reversed(num_list)
<list_reverseiterator object at 0x7fe60d028e90>
>>> list(reversed(num_list))
[18, 6, 6, 36, 65]

# sort排序
>>> sorted(num_list)
[6, 6, 18, 36, 65]
>>> sorted(num_list, reverse=True)  # 降序
[65, 36, 18, 6, 6]

# enumerate返回下标和对应的元素
>>> list(enumerate(num_list))
[(0, 65), (1, 36), (2, 6), (3, 6), (4, 18)]
>>> for data in enumerate(num_list):
...     print(data)
... 
(0, 65)
(1, 36)
(2, 6)
(3, 6)
(4, 18)

>>> for ind, num in enumerate(num_list):
...     print(ind, num)
... 
0 65
1 36
2 6
3 6
4 18

```

## 2.字符串

- 字符编码
  - ASCII (American Standard Code Information Interchange)：美国信息交换标准代码
  - ISO-8859-1：欧洲常用字符编码
  - GB2312/GBK/GB18030：中国采用的字符编码
  - 万国码：unicode。UTF8就是一种实现方式

### (1) 字符串操作符

- 比较操作符：字符串大小按ASCII码值大小进行比较
- 切片操作符：[]、[ : ]、[ : : ]
- 成员关系操作符：in、not in

### (2) 格式化操作符

- 字符串可以使用格式化符号来表示特定含义

| 格式化字符 | 转换方式                      |
| ---------- | ----------------------------- |
| %c         | 转换成字符                    |
| %s         | 优先用str()函数进行字符串转换 |
| %d / %i    | 转成有符号十进制数            |
| %o         | 转成无符号八进制数            |
| %e / %E    | 转成科学计数法                |
| %f / %F    | 转成浮点数                    |

| 辅助指令 | 作用                                          |
| -------- | --------------------------------------------- |
| *        | 定义宽度或者小数点精度                        |
| -        | 左对齐                                        |
| +        | 在正数前面显示加号                            |
| <sp>     | 在正数前面显示空格                            |
| #        | 在八进制数前面显示0，在十六进制前面显示0x或0X |
| 0        | 显示的数字前面填充0而不是默认的空格           |

```python
# 第一列宽度为10，第二列为8
>>> '%10s%8s' % ('name', 'age')
'      name     age'
>>> '%10s%8s' % ('tom', 20)
'       tom      20'

>>> 5 / 3
1.6666666666666667
>>> '%d' % (5/3)
'1'
>>> '%f' % (5/3)
'1.666667'
>>> '%s' % (5/3)
'1.6666666666666667'
>>> '%.2f' % (5/3)
'1.67'  # 保留两位小数
>>> '%06.2f' % (5/3)
'001.67'  # 总宽度为6，小数位2位
>>> '%#o' % 10
'0o12'  # 八进制
>>> '%#x' % 10
'0xa'  # 十六进制

# 科学计数法
>>> '%e' % 1280000
'1.280000e+06'
>>> '%.2e' % 1280000
'1.28e+06'
```

### (3) format函数

- 使用位置函数、使用索引

```python
# 使用位置函数
>>> 'my name is {}, age {}'.format('hoho', 18)
'my name is hoho, age 18'
>>> 'my name is {1}, age {0}'.format(18, 'hoho')
'my name is hoho, age 18'
# 使用索引
>>> 'my name is {0[1]}, age {0[0]}'.format([18, 'hoho'])
'my name is hoho, age 18'
```

- 填充与格式化

```python
{:[填充字符][对齐方式<^>][宽度]}
>>> '{:<10}{:>8}'.format('tom', 20)                                                                              'tom             20' 
# < 左对齐，> 右对齐
```

#### 案例：创建用户

> 1. 编写一个创建用户的功能
> 1. 提示用户输入用户名
> 1. 随机生成8位密码
> 1. 创建用户并设置密码
> 1. 将用户相关信息写入指定文件

```python
import sys
import random
import subprocess
import string

all_chs = string.digits + string.ascii_letters


def gen_pass(n=8):
    # 生成密码
    str_list = [random.choice(all_chs) for i in range(n)]
    return ''.join(str_list)


def add_user(uname, upass, fname):
    # 判断文件是否存在
    isex = subprocess.run(
        'id %s' % uname, shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if isex.returncode == 0:
        return 'error：user %s already exists!' % uname

    # 创建用户
    cr_usr = subprocess.run('useradd %s' % uname, shell=True)
    ch_pw = subprocess.run(
        'echo %s | passwd --stdin %s' % (upass, uname),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # 将信息写入文件
    info = """用户信息：
用户名：%s
密码：%s

""" % (uname, upass)
    with open(fname, 'a') as f:
        f.write(info)
        return 'success'


if __name__ == '__main__':
    uname = sys.argv[1]
    upass = gen_pass()
    fname = '/tmp/users.txt'
    rs = add_user(uname, upass, fname)
    print(rs)
```

(4) 原始字符串操作符

- 原始字符串操作符是为了对付哪些在字符串中出现的特殊字符
- 在原始字符串里，所有的字符都按照字面意思使用，没有转移特殊或不能打印的字符

```python
win_path = 'c:\tmp'
print(win_path)
c:	mp
win_path = 'c:\\tmp'
print(win_path)
c:\tmp
win_path = r'c:\tmp'
print(win_path)
c:\tmp
```

### (5) 内建函数

- string.capitalize()：把字符串的第一个字符大写
- string.center(width)：返回一个原字符串居中，并使用空格填充至长度width的新字符串
- string.counter(str, beg=0, end=len(string))：返回str在string里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
- string.endswith(obj, beg=0, end=len(string))：检查字符串是否以obj结束，如果beg或者end指定则检查指定的范围内是否以obj结束，如果是，返回True，否则返回False
- string.islower()：如果string中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回True，否则返回False
- string.strip()：删除string字符串两端的空白
- string.upper()：转换string中的小写字母为大写
- string.split(str="", num=string.count(str))：以str为分隔符切片string，如果num有指定值，则仅分隔num个子字符串

```python
hi = 'hello world'
print('\t'+hi+'\n')
	hello world
hi = '\t'+hi+'\n'
# 去除两端空白字符
print(hi.strip())
hello world
# 去除左边空白字符
print(hi.lstrip())
hello world
# 去除右边空白字符
print(hi.rstrip())
	hello world
# 对齐
hello = 'hello world'
hello.center(30)
'         hello world          '
hello.center(30, '*')
'*********hello world**********'
hello.ljust(30, '#')
'hello world###################'
hello.rjust(30, '#')
'###################hello world'
# 替换
hello.replace('l', 'm')
'hemmo wormd'
# 分隔，默认为空格
hello.split()
['hello', 'world']
abag = 'hello.tar.gz'
abag.split('.')  # 以.作分隔
['hello', 'tar', 'gz']
# 组合
peaces = abag.split('.')
'-'.join(peaces)
'hello-tar-gz'
''.join(peaces)
'hellotargz'
'_'.join(peaces)
'hello_tar_gz'
# 判断
str_01.islower()  # 都是小写？
True
str_01.isupper()  # 都是大写？
False
str_01.isdigit()  # 都是数字？
False
```

# 4.拓展延伸

## 1.在Linux中运行python脚本

### (1) 使用python执行

- 使用python解释器直接运行对应脚本

### (2) 使用./XX.py执行

- 此种运行方式和shell脚本类似，需要赋予文件执行权限，且在行头加上python解释器路径
- 运行时报错：

```shell
/usr/loacl/bin/python3^M: no such file or directory
# 重点在于^M
# 在windows的pycharm写好的文件，上传到Linux上时，默认行尾是^M格式，可以使用cat -v查看
[root@myproxy Day04]# cat -v subprocess_01.py 
#!/usr/local/bin/python3^M
import subprocess^M
import sys^M
^M
^M
def subr(com, *args):^M
    for i in args:^M
        subprocess.run(com+' '+i, shell=True)^M
^M
^M
if __name__ == '__main__':^M
    print(sys.argv)^M
    com = sys.argv[1]^M
    for i in range(2):^M
        sys.argv.remove(sys.argv[0])^M
    args = sys.argv^M
    print(args)^M
    subr(com, args)^M
```

- 解决方法：
  - 在vim编辑器中修改编码：

```shell
# 查看编码,windows下为dos
:set ff?
fileformat=dos
# 修改编码
:set fileformat=unix
:set ff=unix
```

