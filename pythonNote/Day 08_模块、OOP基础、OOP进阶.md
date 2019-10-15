[TOC]

# 一、模块

## 1.模块和文件

### (1) 什么是模块

+ 模块支持从裸机上组织python代码
+ 当代码量变得相当大的时候，最好把代码分成一些有组织的代码段
+ 代码片段相互间有一定联系，可能是一个包含数据成员和方法的类，也可能是一组相关但彼此独立的操作函数
+ 这些代码段是共享的，所以python允许"调入"一个模块，允许使用其他模块的属性来利用之前的工作城股票，实现代码重用

### (2) 模块文件

+ 说模块是按照逻辑来组织python代码的方法，文件是物理层上组织模块的方法
+ 一个文件被看做是一个独立模块，一个模块也可以被看做是一个文件
+ 模块的文件名就是模块的名字加上扩展名.py

### (3) 名称空间

+ 名称空间就是一个从名称到对象的关系映射集合
+ 给定一个模块名之后，只可能有一个模块被导入到python解释器中，所以在不同模块间不会出现名称交叉现象
+ 每个模块都定义了它自己的唯一名称空间

## 2.导入模块

### (1) 搜索路径

+ 模块的导入需要一个叫做"搜索路径"的过程
+ python在文件系统"预定义区域"中查找要调用的模块
+ 搜索路径在sys.path中定义

```python
>>> import sys
>>> print(sys.path)
['D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\pydev', 'G:\\python\\pycharmContent', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\third_party\\thriftpy', 'D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\helpers\\pydev', 'D:\\pythonWinENV\\python-3.7.4-full\\python37.zip', 'D:\\pythonWinENV\\python-3.7.4-full\\DLLs', 'D:\\pythonWinENV\\python-3.7.4-full\\lib', 'D:\\pythonWinENV\\python-3.7.4-full', 'D:\\pythonWinENV\\python-3.7.4-full\\lib\\site-packages', 'G:\\python\\pycharmContent', 'G:/python/pycharmContent']
```



### (2) 模块导入方法

+ 使用import导入模块
+ 可以在一行导入多个模块，但是可读性会下降
+ 可以只导入模块的某些属性
+ 导入模块时，可以为模块取别名

```python
>>> import time,os,sys
>>> from random import choice
>>> import pickle as p
```

### (3) 导入和加载

+ 当导入模块时，模块的顶层代码会被执行
+ 一个模块不管被导入多少次，只会被加载一次

### (4) 从zip文件中导入

+ 在2.3版本中，python加入了从ZIP归档文件导入模块的功能
+ 如果搜索路径中存在一个包含python模块的.zip文件，导入时会把zip当做目录处理

```python
# 导入sys模块，在搜索路径中加入相应的zip文件
>>> import sys
>>> sys.path.append('/root/pymodule.zip')
>>> import foo  # 导入pymodule.zip压缩文件中的foo模块
```

## 3.包

### (1) 目录结构

+ 包是一个有层次的文件目录结构，为平坦的名称空间加入有层次的组织结构
+ 允许程序员把有联系的模块组合到一起
+ 包目录下必须有一个\__init__.py文件

```python
phone/
    __init__.py
    common_util.py
    voicedata/
        __init__.py
        post.py
```



### (2) 绝对导入

+ 包的使用越来越广泛，很多情况下导入子包会导致和真正的标准库模块发生冲突
+ 因此，所有的导入现在都被认为是绝对的，也就是说这些名字必须通过python路径(sys.path或者PYTHONPATH)来访问

### (3) 相对导入

+ 绝对导入特性使得程序员失去了import的自由，为此出现了相对导入
+ 因为import语句总是绝对导入的，所以相对导入只应用于from-import语句

# 二、OOP基础



# 三、OOP进阶