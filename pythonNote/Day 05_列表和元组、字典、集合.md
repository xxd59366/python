[TOC]

# 一、列表和元组

## 1.列表

### (1) 创建、访问及更新列表

- 列表是有序、可变的数据类型
- 列表中可以包含不同类型的对象
- 列表可以由[]或工厂函数创建
- 支持下标及切片操作

```python
from random import randint
alist = [randint(1,100) for i in range(10)]
alist
[43, 43, 34, 91, 18, 72, 50, 22, 72, 19]
alist[3:5]
[91, 18]
alist[3:5] = [66, 67, 68]  # 改变索引3-5的数
alist
[43, 43, 34, 66, 67, 68, 72, 50, 22, 72, 19]
alist[2:2] = [10, 20]  # 索引为2的位置加上两个数
alist
[43, 43, 10, 20, 34, 66, 67, 68, 72, 50, 22, 72, 19]
```

### (2) 列表内建函数

| 列表方法                | 操作                              |
| ----------------------- | --------------------------------- |
| list.append(obj)        | 像列表中添加一个对象obj           |
| list.count(obj)         | 返回一个对象obj在列表中出现的次数 |
| list.extend(seq)        | 把序列seq的内容添加到列表中       |
| list.index(obj)         | 返回obj对象的下标                 |
| list.insert(index, obj) | 在索引量为index的位置插入对象obj  |
| list.reverse()          | 对列表做倒序操作                  |
| list.sort()             | 排序                              |
| list.pop()              | 默认弹出列表中最后一项            |

```python
alist
[43, 43, 10, 20, 34, 66, 67, 68, 72, 50, 22, 72, 19]
alist.pop()
19
alist
[43, 43, 10, 20, 34, 66, 67, 68, 72, 50, 22, 72]
alist
[43, 43, 10, 20, 34, 66, 67, 68, 72, 50, 22, 72]
alist.pop(-2)
22
alist
[43, 43, 10, 20, 34, 66, 67, 68, 72, 50, 72]
```



## 2.元组

### (1) 创建元组

- 通过()或工厂函数tuple()创建元组
- 元组是有序的、不可变类型
- 与列表相似，作用于列表的操作，绝大多数也能作用于元组

```python
atuple = (10, 20, 30, 20, 40, 20)
atuple
(10, 20, 30, 20, 40, 20)
atuple.count(20)
3
atuple.index(20)
1
```



### (2) 单元素元组

- 如果一个元组中只有一个元素，那么创建该元组的时候，需要加上一个逗号

```python
a = (10)
a
10
type(a)
<class 'int'>
b = (10,)
b
(10,)
type(b)
<class 'tuple'>
len(b)
1
```

### (3) 更新元组

- 虽然元组本身是不可变的，但因为它同时属于容器类型，也就意味着元组的某一个元素是可变的容器类型，那么这个元素中的项目仍然可变

```python
atuple = ('bob', ['bob', 23])
atuple
('bob', ['bob', 23])
atuple[-1]
['bob', 23]
atuple[-1] = ['bob', 22]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
atuple[-1][-1] = 22
atuple
('bob', ['bob', 22])
```

### (4) 案例：用列表构建栈结构

> 1. 栈是一个后进先出的结构
> 1. 编写一个程序，用列表实现栈结构
> 1. 需要支持压栈、出栈、查询功能

```python
stack = []
info = ''


def stack_check():
    """检查状态"""
    info = '开始检查栈状态'
    print(info.center(50, '-'))
    if not stack:
        info = '栈为空，执行压栈操作'
        print(info)
        w_todo(0)
        return
    w_todo()



def w_todo(ch=-1):
    """选择执行分支"""
    info = """栈存在，请选择操作：
压栈：0
出栈：1
查询：2
退出：3
请选择(0/1/2/3)：
"""
    cmds = {0: in_stack(), 1: out_stack(), 2:search()}
    # 用字典调用函数可以提高效率
    cmds[ch]()
    while True:
        if ch == 3:
            return
        ch = int(input(info))
        if ch not in [0, 1, 2, 3]:
            info = '错误输入'
            print(info)
        w_todo(ch)


def in_stack():
    """压栈"""
    info = '执行压栈操作'
    print(info.center(50, '-'))
    info = '请录入元素，输入end...结束：'
    print(info)
    while True:
        elem = input('(end... to quit)> ')
        if elem == 'end...':
            break
        stack.append(elem)
    stack.reverse()
    print('生成栈 %s' % stack)
    stack.reverse()
    stack_check()


def out_stack():
    """出栈"""
    info = '执行出栈操作'
    print(info.center(50, '-'))
    info = '请确认是否出栈，回车确认，输入q退出出栈模式：'
    print(info)
    while True:
        ord = input('(q to quit)> ')
        if ord == 'q':
            break
        if len(stack) == 0:
            info = '栈中元素已全部出栈'
            print(info)
            break
        out = stack.pop()
        print('%s已出栈' % out)
    print(stack)
    stack_check()


def search():
    """查询"""
    info = '执行查询操作'
    print(info.center(50, '-'))
    stack.reverse()
    info = '请输入查询内容，输入q退出：'
    # print(stack)
    while True:
        sear_key = input('(q to quit)> ')
        if sear_key == 'q':
            break
        key_count = stack.count(sear_key)
        if not key_count:
            print('栈中不存在此元素')
            continue
        ind = stack.index(sear_key)
        coo = len(stack) - ind
        info = '内容%s在栈中出现了%s次，最后一次于第%s次加入' % (sear_key, key_count, coo)
        print(info)
    stack.reverse()
    w_todo()


if __name__ == '__main__':
    stack_check()
```



# 二、字典

## 1.字典基础操作

### (1) 创建字典

- 通过{}操作符创建字典
- 通过dict()工厂方法创建字典
- 通过fromkeys()创建具有相同值的默认字典
- 字典的key只能是不可变对象(数字、字符串、元组)

```python
dict()
{}
adict = {'name':'bob', 'age':23}
adict
{'name': 'bob', 'age': 23}
bdict = dict([['name', 'bob'], ['age', 23]])
bdict
{'name': 'bob', 'age': 23}
cdict = {}.fromkeys(['bob', 'alice'], 23)
cdict
{'bob': 23, 'alice': 23}
ddict = {}
# 列表不能做key
ddict[[1, 2]] = 10
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
# 元组可以作为key值，表示坐标
ddict[(1, 2)] = 10
ddict
{(1, 2): 10}
```

### (2) 访问字典

- 字典是映射类型，意味着它没有下标，访问字典中的值需要使用相应的键

```python
# 占位符访问
'%(name)s: %(age)s %(email)s' % adict
'bob: 20 bob@test.com'
```

### (3) 更新字典

- 通过键更新字典
  - 如果字典中有该键，则更新相关值
  - 如果字典中没有该键，则向字典中添加新值
  - 因此，字典中的key没有重复值

```python
adict
{'name': 'bob', 'age': 23}
# 已存在的键，更改其值
adict['age'] = 20
adict
{'name': 'bob', 'age': 20}
# 没有的键，添加新值
adict['email'] = 'bob@test.com'
adict
{'name': 'bob', 'age': 20, 'email': 'bob@test.com'}
```

### (4) 删除字典

- 通过del可以删除字典中的元素或者整个字典
- 使用内部方法clear()可以清空字典
- 使用pop()方法可以弹出字典中的元素

```python
adict
{'name': 'bob', 'age': 20, 'email': 'bob@test.com'}
# 删除email键
del adict['email']
adict
{'name': 'bob', 'age': 20}
# 取出age
adict.pop('age')
20
adict
{'name': 'bob'}
# 清空字典
adict.clear()
adict
{}
```

### (5) 字典操作符

- 使用字典查找操作符[]，查找键所对应的值
- 使用in和not in判断键是否存在于字典中

```python
# 此语句验证的是字典中的key值
'bob' in adict
False
'name' in adict
True
```

## 2.字典相关函数

### (1) 作用于字典的函数

- len()：返回字典中元素的数目

```python
bdict
{'name': 'bob', 'age': 23}
len(bdict)
2
```

- hash()：本身不是为字典设计的，但是可以判断某个对象是否可以作为字典的键

```python
hash(3)
3
hash([1, 2])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
```

### (2) 字典的内建方法

- dict.copy()：返回字典(深复制)的一个副本
- dict.get(key, default=None)：对字典dict中的键key，返回它对应的值value，如果字典中不存在此键，则返回default值，default默认值为None
- dict.items()：返回一个包含字典汇总键值对元组的列表
- dict.keys()：返回一个包含字典中键的列表
- dict.values()：返回一个包含字典中所有值的列表
- dict.update(dict2)：将字典dict2的键值对添加到字典dict

```python
# 取出键值对
bdict.items()
dict_items([('name', 'bob'), ('age', 23)])
# 遍历字典
for key, val in bdict.items():
    print(key, val)
    
name bob
age 23
# 只取出key
bdict.keys()
dict_keys(['name', 'age'])
# 只取出值
bdict.values()
dict_values(['bob', 23])
# 更新字典
bdict.update({'qq':'123456789', 'phone':'123456789001'})
bdict
{'name': 'bob', 'age': 23, 'qq': '123456789', 'phone': '123456789001'}
bdict.update({'name':'tom'})
bdict
{'name': 'tom', 'age': 23, 'qq': '123456789', 'phone': '123456789001'}
# 弹出一项
bdict.popitem()
('phone', '123456789001')
# 获取对应键的值
bdict['birth_date']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'birth_date'
# get默认返回none
bdict.get('birth_date')
# 设定默认值，取到值则返回值，取不到则返回默认
bdict.get('birth_date', 'not found')
'not found'
bdict.get('age', 30)
23
```

### (3) 案例：模拟用户登录信息系统

> 1. 支持新用户注册，新用户名和密码注册到字典中
> 1. 支持老用户登录，用户名和密码正确提示登陆成功
> 1. 主程序通过循环询问进行何种操作，根据用户的选择，执行注册或是登录操作

```python
import getpass
userdb = {}

def register():
    print('register'.center(50, '-'))
    uname = input('username: ')
    if uname in userdb:
        print('\033[31;1musername already exists, try again.\033[0m')
    else:
        pw = input('password: ')
        userdb[uname] = pw

def login():
    print('login'.center(50, '-'))
    uname = input('username: ')
    pw = getpass.getpass('password: ')
    if userdb.get(uname) == pw:
        print('\033[32;1msuccess!\033[0m')
    else:
        print('\033[31;1minvalid login!\033[0m')


def show_menu():
    prompt = """(0) 退出
(1) 注册
(2) 登录
"""
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('invalid input, try again please!')
            continue

        if choice == '0':
            print('Bye!')
            break

        cmds = {'1': register, '2': login}
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
```

## 3.集合

### (1) 创建集合

- 数学上，把set称作由不同元素组成的集合，集合(set)的成员通常被称作集合元素
- 集合对象是一组无序排列的可哈希的值，可以理解为没有value的字典
- 集合有两种类型
  - 可变集合set
  - 不可变集合frozenset
- 字典和集合都是无序的，字典的key和集合元素都是不可变的、不能重复的

```python
fs = frozenset('abc')
s1 = set('abc')
fs
frozenset({'b', 'a', 'c'})
s1
{'b', 'a', 'c'}
```

### (2) 集合类型操作符

- 集合支持用in和not in操作符检查成员
- 能够通过len()检查集合大小
- 能够使用for迭代集合成员
- 不能取切片，没有键
- |：联合，取并集
- &：交集
- -：差补

```python
s10 = set(['aaa', 'bbb', 'ccc'])
s10
{'aaa', 'bbb', 'ccc'}
len(s10)
3
for word in s10:
    print(word)
    
aaa
bbb
ccc
# 操作符，或与非
s1 = set('abc')
s2 = set('cde')
s1 | s2  # 取并集
{'c', 'b', 'a', 'e', 'd'}
s1 & s2  # 取交集
{'c'}
s1 - s2  # 取差补
{'b', 'a'}
```



### (3) 集合内建方法

- set.add()：添加成员
- set.update()：批量添加成员
- set.remove()：移除成员
- s.issubset(t)：如果s是t的子集，则返回True，否则返回False
- s.issuoerset(t)：如果t是s的超集，则返回True，否则返回False
- s.intersection(t)：返回一个新集合，该集合是s和t的交集
- s.difference(t)：返回一个新集合，该集合是s的成员，但不是t的成员

```python
# add将元素整体加入集合
s1.add('new')
s1
{'b', 'a', 'new', 'c'}
# 将对象中每个元素拆分加入集合
s1.update('new')
s1
{'new', 'b', 'n', 'w', 'c', 'a', 'e'}
# 通过列表形式添加
s1.update(['hello', 'world'])
s1
{'new', 'b', 'world', 'n', 'w', 'c', 'a', 'e', 'hello'}
# 移除new
s1.remove('new')
s1
{'b', 'world', 'n', 'w', 'c', 'a', 'e', 'hello'}
# 超集和子集
s2 = {'a', 'b', 'c'}
s2
{'b', 'a', 'c'}
s1.issuperset(s2)  # s1是s2的超集
True
s2.issubset(s1)  # s2是s1的子集
True
s1.union(s2)  # 等同于s1 | s2
{'b', 'world', 'n', 'w', 'c', 'a', 'e', 'hello'}
s1.intersection(s2)  # 等同于s1 & s2
{'b', 'a', 'c'}
s1.difference(s2)  # 等同于s1 - s2
{'world', 'n', 'w', 'e', 'hello'}
```

### (4) 集合的应用

- 去重：

```python
import random
num_list = [random.randint(1, 20) for i in range(10)]
num_list
[17, 11, 3, 12, 14, 6, 2, 5, 4, 6]
set(num_list)
{2, 3, 4, 5, 6, 11, 12, 14, 17}
list(set(num_list))  # 返回列表
[2, 3, 4, 5, 6, 11, 12, 14, 17]
```

#### 案例：比较文件内容

> 1. 比较两个文件a.log和b.log的内容
> 1. 两个文件有大量的重复
> 1. 取出只有b.log的值

```python
def diff_out(fname_1, fname_2, rsname):
    with open(fname_1) as f1:
        aset = set(f1)
    with open(fname_2) as f2:
        bset = set(f2)
    with open(rsname, 'w') as rs:
        rs.writelines(bset - aset)

if __name__ == '__main__':
    fname_1 = ''
    fname_2 = ''
    rsname = ''
    diff_out(fname_1, fname_2, rsname)
```

