[TOC]

# **一、Python概述**

## **1.Python简介**

### **(1) Python起源**

· 由Guido van Rossum与1989年底创始

· 1991年初，Python发布了第一个公开发行版

· 为了更好的完成荷兰的CWI(国家数学和计算机科学院)的一个研究项目而创建

### **(2) Python版本**

· Python2.x

​	\- 目前所有系统默认安装的版本

· Python3.x

​	\- 2009年2月13日发布

​	\- 在语法和功能上有较大调整

​	\- Python的发展趋势

### **(3) Python特点**

· 高级：有高级的数据结构，缩短开发时间与代码量

· 面向对象：为数据和逻辑相分离的结构化和过程化变成添加了新的活力

· 可升级：提供了基本的开发模块，可以在它上面开发软件，实现代码重用

· 可扩展：通过将其分离为多个文件或模块加以组织管理

· 可以执行：python是用C写的，由于C的可移植性，使得python可以运行在任何带有ANSI C编译器的平台上

· 易学：python关键字少、结构简单、语法清晰

· 易读：没有其他语言通常用来访问变量、定义代码块和进行模式匹配的命令式符号

· 内存管理器：内存管理是由python解释器负责的

# **二、环境准备**

## 1.安装与配置

### (1) 获取python3源码

· 官方站点

​	\- http://www.python.org

· 选择正确的系统

· 选择正确的版本

### (2) 安装python3

· 安装依赖包

```shell
$ yum install -y gcc gcc-c++ zlib-devel openssl-devel readline-devel libffi-devel sqlite-devel tcl-devel tk-devel
```

· 安装python3

```shell
$ tar xzf Python-3.6.4.tar.gz
$ cd Python-3.6.4
$ ./configure --prefix=/usr/local
$ make && make install
```



### (3) 设置环境变量

· Python虚拟环境：虚拟环境相当于把Python隔离到一个目录中，安装软件包时，都安装到虚拟环境目录，将来项目结束后，直接把虚拟环境目录删除即可

· 创建虚拟环境

```shell
$ python3 -m venv ~/nsd1902
$ ls ~/nsd1902
### 激活虚拟环境 ###
$ source ~/nsd1902/bin/activate
$ python --version
Python 3.6.7
```

· 运行python

​	\- 交互解释器(IDLE)

```shell
$ python
>>> print('Hello World!')
Hello World!
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>>
```

​	\- 文件形式

```shell
$ vim /tmp/hello.py
print('Hello World!')
$ python /tmp/hello.py
Hello World!
```



### (4) 设置pycharm

· Pycharm是由JetBrains打造的一款Python IDE

· 支持的功能有：

​	\- 调试、语法高亮

​	\- Project管理、代码跳转

​	\- 智能提示、自动完成

​	\- 单元测试、版本控制

· 下载地址：

http://www.jetbrains.com/pycharm/download

· 分为专业版和社区版

1. 删除pycharm配置

```shell
$ rm -rf ~/..PyCharm2017.3
```

2. 启动pycharm
   1. don't import settings
   2. 企业版输入License
   3. 输入python解释器(Pycharm Interpreter)位置
   4. 修改编辑器文字大小：File -> Settings -> Editor -> Font

# **三、使用Git**

## 1.本地操作

### (1) Git简介

· Git是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目

· Git是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开源版本控制软件

· 与常用的版本控制工具CVS，Subversion不同，Git采用分布式版本库的方式，不必要服务器端软件支持

### (2) 安装及配置

· Git安装后需要配置用户相关信息

```shell
$ yum install -y git
$ git config --global user.name "Mr.Zhang"
$ git config --global user.email "zhangzg@tedu.cn"
$ git config --global core.editor vim
$ git config --list
$ cat ~/.gitconfig
```

### (3) Git工作流程

![1568617891604](G:\pythonNote\Day01\1568617891604.png)

### (4) 工作区、暂存区和版本库

· 工作区：电脑里能看到的目录

· 暂存区：stage或index。一般存放在.git目录下的index文件(.git/index)中，所以我们把暂存区也叫作索引

· 版本库：工作区有一个隐藏目录.git，这个不算工作区，而是git版本库

![1568618112543](G:\pythonNote\Day01\1568618112543.png)

### (5) 创建仓库

· git使用git init命令来初始化一个git仓库，git的很多命令都需要在Git的仓库中运行，所以git init是使用git的第一个命令

```shell
$ mkdir devops
$ cd devops/
$ git init
# 或者
$ git init devops
```

### (6) 添加文件到暂存区

· 添加指定文件

```shell
$ echo 'print("hello world!")' > hello.py
$ git add hello.py
$ git status
```

· 添加所有文件

```shell
$ cp hello.py welcome.py
$ git add .
$ git status -s
```

### (7) 确认至仓库

· 提交前需要设置用户信息

```shell
$ git commit -m "初始化仓库"
$ git status
```

· 添加追踪文件并提交到版本库

```shell
$ echo 'print("done.")' >> hello.py
$ git commit -am "向hello.py添加新行"
```

### (8) 删除跟踪文件

· 要从git中移除某个文件，就必须要从已跟踪文件清单中移除，然后提交

```shell
$ git ls-files # 查看版本库中文件
$ git rm welcome.py
$ git commmit -m '删除welcome.py'
```

### (9) 案例

> 1. 创建devops目录
> 1. 为devops创建git目录
> 1. 新建文件hello.py，并将文件初始化到仓库中
> 1. 修改hello.py并将其更新到仓库
> 1. 从库中删除hello.py

```shell
# 创建devops目录
[root@myproxy git]# mkdir devops

# 为devops创建Git目录
[root@myproxy git]# cd devops/
[root@myproxy devops]# git init
[root@myproxy devops]# ls -A
.git

# 新建hello.py文件并初始化到仓库中
[root@myproxy devops]# echo 'print("hello world!")' > hello.py
[root@myproxy devops]# git config user.name 'yyzh_cn'
[root@myproxy devops]# git config user.email 'yyzh_cn@proxy.com'
[root@myproxy devops]# git add .
[root@myproxy devops]# git commit -m '初始化仓库'

# 修改hello.py并将其更新到库
[root@myproxy devops]# echo 'print("# exit")' >> hello.py 
[root@myproxy devops]# git commit -am '添加新行到hello.py'
[master c781fd3] 添加新行到hello.py
 1 file changed, 1 insertion(+)
 
# 从库中删除hello.py
[root@myproxy devops]# git ls-files
hello.py
[root@myproxy devops]# git rm hello.py
rm 'hello.py'
[root@myproxy devops]# git commit -m '删除hello.py'
[master c82efb4] 删除hello.py
 1 file changed, 2 deletions(-)
 delete mode 100644 hello.py
```

## 2.使用远程服务器

### (1) 搭建本地gitlab服务器

· 导入中文版gitlab镜像

```shell
$ docker load < /path/to/gitlab_zh.tar
```

· 将物理主机ssh端口改为2022后，启动容器

```shell
$ docker run -d -h gitlab --name gitlab \
-p 443:443 -p 80:80 -p 22:22 --restart always \
-v /srv/gitlab/config:/etc/gitlab -v /srv/gitlab/logs:/var/log/gitlab -v /srv/gitlab/data:/data \
gitlab_zh:latest
```

### (2) 初始化gitlab服务器

· 密码需大于8位

![1568620850430](G:\pythonNote\Day01\1568620850430.png)

· 默认用户名为root

![1568620919112](G:\pythonNote\Day01\1568620919112.png)

### (3) 添加gitlab项目

· 创建群组group

- 使用群组管理项目和人员是非常好的方式

· 创建项目project

- 存储代码的地方，里面还包含问题列表、wiki文档以及其他一些gitlab功能

· 创建成员member

- 添加你的团队成员或其他人员到Gitlab

### (4) 创建群组

### (5) 创建项目

### (6) 创建用户

· 创建用户后，再次编辑可设置密码

· root用户将新用户加入组中，并设置新用户为"主程序员"

· 新用户初次登陆需要设置自己的密码

### (7) 用户管理

· 将本地生成的公钥上传至服务器

· 将本地仓库推送至服务器

```shell
$ git remote rename origin old-origin
$ git remote add origin
git@192.168.113.249：/devops/core_py.git
$ git push -u origin --all
```

· 添加新文件

```shell
$ echo '# this is a test' > hi.py
$ git add hi.py
$ git commit hi.py -m '新的测试'
$ git push origin master
```

· 代码下载到本地

```shell
$ git clone
git@192.168.113.249:devops/core_py.git
$ ls -A core_py/
.git hello.py hi.py
```

· 更新代码到本地

```shell
$ git pull
```

> 1. 通过docker搭建gitlab服务器
> 1. 新建群组devops
> 1. 新建项目页core_py
> 1. 新建用户，其在devops组中为主程序员
> 1. 新用户上传版本库到gitlab
> 1. 熟悉git远程操作方法、

```shell
# 服务器太小，懒得搭了~ 摸了摸了-。-
```

# **四、Python起步**

## 1、Python语法基础

### (1) 语句块缩进

· python代码块通过缩进对其表达代码逻辑而不是使用大括号

· 缩进表达一个语句属于哪个代码块

· 缩进风格

​	\- 1或2：可能不够，很难确定代码语句属于哪个块

​	\- 8至10：可能太多，如果代码内嵌的层次太多，就会使得代码很难阅读

​	\- 4个空格：非常流行，范·罗萨姆支持的风格

· 缩进相同的一组语句构成一个代码块，称之为代码组

· 首行以关键字开始，以冒号：结束，该行之后的一行或多行代码构成代码组

· 如果代码组只有一行，可以将其直接写在冒号后面，但是这样的写法可读性差，不推荐

### (2) 注释及续行

· 首要说明的是：尽管Python是可读性最好的语言之一，这并不意味着程序员在代码中就可以不写注释

· 和很多UNIX脚本类似，python注释语句从#字符开始

· 注释可以在一行的任何地方开始，解释器会忽略掉该行#之后的所有内容

· 一行过长的语句可以使用反斜杠\分解成几行

### (3) 同行多个语句

· 分号; 允许你将多个语句写在同一行上

· 但是这些语句不能在这行开始一个新的代码块

· 因为可读会变差，所以不推荐使用

### (4) 输出语句

· 获取帮助

```python
>>> help(print)
```

· 使用方式

```python
>>> print('Hello World!')
Hello World!
>>> print('Hello' + 'World!')
HelloWorld!
>>> print('Hello', 'World!')
Hello World!
>>> print('Hello', 'World!',sep='***')
Hello***World!
>>> print('Hello', 'World!',sep='***',end='123')
Hello***World!123
```

### (5) 输入语句

· 获得帮助

```python
>>> help(input)
```

· 使用方式( 注意，input的返回值一定是字符类型 )

```python
>>> num = input("Number:")
Number: 20
>>> num + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number' is not defined
```

## 2、Python变量

### (1) 变量定义

· 变量名称约定

​	\- 第一个字符只能是大小写字母或下划线

​	\- 后续字符只能是大小写字母或数字或下划线

​	\- 区分大小写

· python是动态类型语言，即使不需要预先声明变量的类型

· 推荐采用的全名方法

​	\- 变量名全部采用小写字母

​	\- 简短、有意义

​	\- 多个单词间用下划线分隔

​	\- 变量名用名词，函数名用谓词(动词+名词)

​	\- 类名采用驼峰形式

### (2) 变量赋值

· 变量在使用之前必须赋值

· 变量在赋值时决定它是什么类型

· 变量的类型和值在赋值那一刻被初始化

· 变量赋值通过等号来执行

```python
>>> counter = 0
>>> name = 'bob'
```

· python也支持增量赋值

```python
>>> n += 1
# 等价于于n = n + 1
>>> n *= 1
# 等价于n = n * 1
>>> i++
>>> a = 9
>>> a++
  File "<stdin>", line 1
    a++
      ^
SyntaxError: invalid syntax
>>> ++a
9
# python不支持a++这种写法，++a中的+只代表正号
```

### (3) 运算符

· 标准算术运算符

| **标准算术符** | +       | -       | *      | /      | //     | %      | **     |
| -------------- | ------- | ------- | ------ | ------ | ------ | ------ | ------ |
| **比较运算符** | **<**   | **<=**  | **>**  | **>=** | **==** | **!=** | **<>** |
| **逻辑运算符** | **and** | **not** | **or** |        |        |        |        |

```python
# divmod函数求商和余数
>>> divmod(5,3)
(1, 2)
>>> a, b = divmod(5,3)
# 把商和余数分别赋值给变量a 和 b
>>> a
1
>>> b
2
# **代表乘方，做幂运算
>>> 2 ** 3
8
>>> 3 * 2 ** 3
24
# 幂运算的优先级较高
>>> 3 * (2 ** 3)
24
# 一般使用括号来区分优先级
```

## 3.数据类型概述

### (1) 数字

#### · 基本数字类型

| 类型    | 描述                      |
| ------- | ------------------------- |
| int     | 有符号整数                |
| bool    | 布尔值(True为1，False为0) |
| float   | 浮点数                    |
| complex | 复数                      |

#### · 数字表示方式

- python默认以十进制数显示

- 数字以0o或0O开头表示为8进制数

- 数字以0x或0X开头表示16进制数

- 数字以0b或0B开头表示2进制数

```python
[root@myproxy ~]# cp /etc/hosts /tmp
[root@myproxy ~]# ll /tmp/hosts
-rw-r--r-- 1 root root 251 Sep 15 22:00 /tmp/hosts
>>> import os
>>> os.chmod('/tmp/hosts',600)
[root@myproxy ~]# ll /tmp/hosts 
---x-wx--T 1 root root 251 Sep 15 22:00 /tmp/hosts
>>> os.chmod('/tmp/hosts', 0o600)
[root@myproxy ~]# ll /tmp/hosts 
-rw------- 1 root root 251 Sep 15 22:00 /tmp/hosts
# Linux文件权限是8进制
```

### (2) 序列对象

### · 字符串

#### · 定义字符串

- python中字符串被定义为引号之间的字符集合
- python支持使用成对的单引号和双引号
- 无论单引号还是双引号，表示的意义是相同的
- python还支持三引号(三个连续的单引号或者双引号)，可以用来包含特殊字符
- python不区分字符和字符串

```python
# 多类型变量输出时使用占位符
>>> name = 'tom'
>>> age = 20
>>> "%s is %s years old." % ( name, age)
# 三引号的使用可以保留用户的输入格式
>>> words = "hello\nwelcome\ngreet"
>>> print(words)
hello
welcome
greet
### 上面的可读性太差，使用三引号等价表达 ###
>>> wds = '''hello
... welcome
... greet'''
>>> print(wds)
hello
welcome
greet
>>> wds
'hello\nwelcome\ngreet'
```



#### · 字符串切片

· 使用索引运算符[]和切片运算符[ : ]可得到子字符串

· 第一个字符的索引是0，最后一个字符的索引是-1

· 子字符串包含切片汇总的起始下标，但不包含结束下标

```python
>>> py_str = 'python'
>>> len(py_str)
6
>>> py_str[0]
'p'
# 负数表示从右往左取值
>>> py_str[-2]
'o'
>>> py_str[2:4]
'th'
>>> py_str[2:]
'thon'
>>> py_str[:4]
'pyth'
# 步长为2
>>> py_str[::2]
'pto'
>>> py_str[1::2]
'yhn'
```

#### · 字符串连接操作

· 使用+号可以将多个字符串拼接在一起

· 使用*号可以将一个字符串重复多次

```python
>>> is_cool =  'is Cool'
>>> print(py_str + '' + is_cool)
pythonis Cool
>>> py_str * 2
'pythonpython'
```

### · 列表和元组

#### · 定义列表

· 可以将列表当成普通的"数组"，它能保存任意数量的任意类型的python对象

· 像字符串一样，列表也支持下标和切片操作

· 列表中的项目可以改变

```python
>>> alist = [1, "tom", "alice"]
>>> alist[1] = 'bob'
>>> alist
[1, 'bob', 'alice']
```

#### · 列表操作

· 使用in或not in判断成员关系

· 使用append方法向列表中追加元素

```python
>>> len(alist)
3
>>> alist + [100]
[1, 'bob', 'alice', 100]

```

#### · 元组的定义及操作

· 可以认为元组是"静态的列表"

· 元组一旦定义，不能改变

```python
>>> atuple = (10, 20, 30, 'tom', 'jerry', 100)
>>> atuple[1]
20
>>> atuple[-1]
100
>>> atuple[2:4]
(30, 'tom')
>>> len(atuple)
6
>>> atuple[-1] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# 报错，元组中元素不能改变
```

### (3) 字典

#### · 字典的定义及操作

· 字典是由无序的键值对(key-value)构成的映射数据类型

· 通过键来取值，不支持下标操作

```python
>>> adict = {'name': 'bob', 'age': 20}
>>> 'bob' in adict
False
>>> 'name' in adict
True
>>> adict['name']
'bob'
>>> adict
{'age': 20, 'name': 'bob'}
```

#### · 数据类型比较(重点)

· 按存储模型分类：

- 标量：数字、字符串
- 容器：列表、元组、字典

· 按更新模型分为

- 不可变：数字、字符串、元组

- 可变：列表、字典

```python
>>> s1 = 'python'
>>> alist = [1, 2, 3]
>>> s1[0]
'p'
>>> alist[0]
1
>>> alist[0] = 10
>>> s1[0] = 'P'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
# 因为字符串不可变，所以报错，需要整体修改
>>> s1 = 'Python'
```

· 按访问模型分

- 直接：数字
- 顺序：字符串、列表、元组
- 映射：字典

