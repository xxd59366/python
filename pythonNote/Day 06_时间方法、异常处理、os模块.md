[TOC]



# 一、时间方法

## 1.time模块

### (1) 时间表示方式

- 时间戳timestamp：表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
- UTC(Coordinated Universal Time，世界协调时)亦即格林威治天文时间，世界标准时间。在中国为UTC+8.DST(Daylight Saving Time)即夏令时
- 元组(struct_time)：由9个元素组成

### (2) struct_time元组

| 索引 | 属性                    | 值             |
| ---- | ----------------------- | -------------- |
| 0    | tm_year                 | 2000           |
| 1    | tm_mon                  | 1-12           |
| 2    | tm_mday                 | 1-31           |
| 3    | tm_hour                 | 0-23           |
| 4    | tm_min                  | 0-59           |
| 5    | tm_sec                  | 0-61           |
| 6    | tm_wday                 | 0-6(0表示周一) |
| 7    | tm_yday(一年中的第几天) | 1-366          |
| 8    | tm_isdst(是否为dst时间) | 默认为-1       |

### (3) time模块方法

- time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未听过，则以当前时间为准。
- time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区(0时区)的truct_time。
- time.time()：返回当前时间的时间戳
- time.mktime(t)：将一个struct_time转化为时间戳
- time.sleep(secs)：线程推迟指定的时间运行，单位为秒
- time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入
- time.ctime([secs])：把一个时间戳(按秒计算的浮点数)转化为time.asctime()的形式
- time.strftime(format[, t])：把一个代表时间的元组或者struct_time(如由time.licaltime()和time.gmtime()返回)转化为格式化的时间和字符串。如果t未指定，将传入time.localtime()
- time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作

```python
import time
# 返回当前的时间戳
>>> time.time()
1569387998.5116668
# 返回世界协调时
>>> time.ctime()
'Wed Sep 25 13:18:53 2019'
# 九元组struct_time
>>> time.localtime()
time.struct_time(tm_year=2019, tm_mon=9, tm_mday=25, tm_hour=13, tm_min=20, tm_sec=16, tm_wday=2, tm_yday=268, tm_isdst=0)
>>> t = time.localtime()
>>> t.tm_year
2019
>>> time.localtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)  # 因为是东8区，所以tm_hour=8
# sleep
>>> time.sleep(3)
```

### (4) 时间样式

| 格式 | 含义                                | 格式 | 含义                                          |
| ---- | ----------------------------------- | ---- | --------------------------------------------- |
| %a   | 本地简化星期名称                    | %m   | 月份(01-12)                                   |
| %A   | 本地完整星期名称                    | %M   | 分钟数(00-59)                                 |
| %b   | 本地简化月份名称                    | %p   | 本地am或者pm的相应符                          |
| %B   | 本地完整月份名称                    | %S   | 秒(01-61)                                     |
| %c   | 本地相应的日期和时间                | %U   | 一年中的星期数(00-53，星期日是一个星期的开始) |
| %d   | 一个月中的第几天                    | %w   | 一个星期中的第几天                            |
| %H   | 一天中的第几个小时(24小时制，00-23) | %x   | 本地相应日期                                  |
| %l   | 第几个小时(12小时制，01-12)         | %X   | 本地相应时间                                  |
| %j   | 一年中的第几天(001-366)             | %y   | 去掉世纪的年份(00-99)                         |
| %Z   | 时区的名字                          | %Y   | 完整的年份                                    |

```python
# 转成指定字符串格式(年月日时分秒)
>>> time.strftime('%Y-%m-%d %H:%M:%S')
'2019-09-25 13:45:04'
# 字符串转成九元组格式
>>> time.strptime('2019-09-25 13:45:04', '%Y-%m-%d %H:%M:%S')
time.struct_time(tm_year=2019, tm_mon=9, tm_mday=25, tm_hour=13, tm_min=45, tm_sec=4, tm_wday=2, tm_yday=268, tm_isdst=-1)
```

### (5) 案例：从日志文件中提取9点到12点的内容

```python
import time

logfile = 'web_log'
t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open(logfile) as f:
    for line in f:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t >= t9:
            print(line, end='')
```

## 2.datetime模块

### (1) datetime模块方法

- datetime.today()：返回一个表示当前本地时间的datetime对象
- datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间
- datetime.ctime(datetime对象)：返回时间格式字符串
- datetime.strftime(format)：返回指定格式字符串

```python
# datetime格式比起time来要精简很多
>>> import datetime
>>> t1 = datetime.datetime.now()
>>> t1
datetime.datetime(2019, 9, 25, 21, 22, 28, 428785)
# 上面写得太长，直接从模块中导入datetime
>>> from datetime import datetime
>>> t1 = datetime.now()
>>> t1  # 显示为年月日时分秒毫秒
datetime.datetime(2019, 9, 25, 21, 22, 56, 716218)
# t1的属性
>>> t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second, t1.microsecond
(2019, 9, 25, 21, 22, 28, 428785)
# 将datetime对象转换成时间字符串
>>> datetime.datetime.strftime(t1,'%Y-%m-%d %H:%M:%S')
'2019-09-25 21:22:28'
# 将时间字符串转成datetime对象
>>> datetime.datetime.strptime('2019-09-25 21:22:28', '%Y-%m-%d %H:%M:%S') 
datetime.datetime(2019, 9, 25, 21, 22, 28)
# 不需要全部写全
>>> t = datetime.datetime(2019, 10, 1)
>>> t
datetime.datetime(2019, 10, 1, 0, 0)
```

### (2) 时间计算

- 使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微秒的时间计算

```python
# 计算时间差额
>>> dt = datetime.datetime.now()
>>> days = datetime.timedelta(days=100, hours=3)  # 时间差
>>> dt += days
>>> dt
datetime.datetime(2020, 1, 4, 0, 57, 19, 457858)
>>> datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
'2020-01-04 00:57:19'
```



# 二、异常处理

## 1.异常

### (1) 什么是异常

- 当python检测到一个错误时，解释器就会指出当前流已经无法继续执行下去，这时候就出现了异常
- 异常是因为程序出现了错误而在正常控制流意外采取的行为
- 这个行为分为两个阶段：
  - 引起异常发生的错误
  - 检测和采取可能的应对措施

### (2) python中的异常

- 当程序运行时，因为遇到未解的错误而导致终止运行，便会出现traceback消息，打印异常

| 异常              | 描述                      |
| ----------------- | ------------------------- |
| NameError         | 未声明/初始化对象         |
| IndexError        | 序列中没有此索引          |
| SyntaxError       | 语法错误                  |
| KeyboardInterrupt | 用户中断执行              |
| EOFError          | 没有内建输入，到达EOF标记 |
| IOError           | 输入/输出操作失败         |

### (3) try-expect语句

- 定义了进行异常监控的一段代码，并且提供了处理异常的机制
- 可以把多个except语句连接在一起，处理一个try块中可能发生的多种异常

```python
try:
    num = int(input('number: '))
    result = 100/num
    print('Done')
except ValueError:
    print('无效的输入')
except ZeroDivisionError:
    print('无效的输入')
except KeyboardInterrupt:
    print('\nBye')
except EOFError:
    print('\nBye')
# 对于相同处理方式的异常，可以使用元组形式处理
try:
    num = int(input('number: '))
    result = 100/num
    print('Done')
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye')
```

### (4) 异常返回值、else与finally语句

```python
try:
    num = int(input('number: '))
    result = 100/num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
    exit(60)
except (KeyboardInterrupt, EOFError):
    print('\nBye')
    exit(65)
else:
    print(result)
finally:
    print('Done')

print('正常结束')
```

```python
try:
    有可能发生异常的语句
except 异常名字:
    处理异常的代码
else:
    不发生异常才执行的代码
finally:
    不管异常是否发生都要执行的代码
```



### (5) 异常参数

- 异常也可以有参数，异常发生后它会被传递给异常处理器
- 当异常被引发后参数是作为附加帮助信息传递给异常当处理器的

```python
# 将系统原本的报错信息保存到变量e中
try:
    num = int(input('number: '))
    result = 100/num
except (ValueError, ZeroDivisionError) as e:
    print('无效的输入: ', e)
    exit(60)
```

## 2.触发异常

### (1) raise语句

- 想要引发异常，最简单的形式就是输入关键字raise，后面跟上想要引发的异常的名称
- 执行raise语句时，Python会创建指定的异常类的一个对象
- raise语句还可以指定对异常对象进行初始化的参数'

```python
def set_age(name, age):
    if not 0 < age < 120:
        raise Exception('年龄超出范围')
    print('%s is %s years old.' % (name, age))


if __name__ == '__main__':
    set_age('yyl', 266)
```

### (2) 断言

- 断言是一句必须等价于布尔值为真的判定
- 表达式为假，发生异常

```python
def set_age2(name, age):
    assert 0 < age < 120, '年龄超出范围(1-120)'
    print('%s is %s years old.' % (name, age))

    
if __name__ == '__main__':
    set_age2('sb', 255)
```

# 三、OS相关模块

## 1.os模块

### (1) os模块简介

- 对文件系统的访问大多通过python的os模块实现
- 该模块是python访问操作系统弄能的主要接口
- 有些方法，如copy等，并没有提供，可以使用shutil模块作为补充

### (2) OS模块方法

| 函数       | 作用               |
| ---------- | ------------------ |
| symlink()  | 创建符号链接       |
| listdir()  | 列出指定目录的文件 |
| getcwd()   | 返回当前工作目录   |
| mkdir()    | 创建目录           |
| chmod()    | 改变权限模式       |
| getatime() | 返回最近访问时间   |
| chdir()    | 改变工作目录       |
| remove()   | 删除文件           |
| unlink()   | 删除软链接         |

```python
>>> import os
>>> os.getcwd()
'G:\\python\\pycharmContent'
>>> os.listdir()
['.idea', 'Day01', 'Day02', 'Day03', 'Day04', 'Day05', 'Day06', 'else']
>>> os.makedirs('tmp/mydemo/mydir')  # mkdir -p
>>> os.mkdir('test')
>>> os.listdir()
['.idea', 'Day01', 'Day02', 'Day03', 'Day04', 'Day05', 'Day06', 'else', 'test', 'tmp']
#### touch
>>> os.mknod('hello')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: module 'os' has no attribute 'mknod'
####
>>> os.chmod('test', 0o644)
>>> os.rename('test', 'hello')
>>> os.rmdir('hello')
```

- os.path子模块

```python
# 当前路径
>>> os.path.abspath('.')
'G:\\python\\pycharmContent'
>>> os.chdir('tmp')
>>> os.getcwd()
'G:\\python\\pycharmContent\\tmp'
# 路径切割
>>> os.path.dirname('G:\\python\\pycharmContent\\tmp')
'G:\\python\\pycharmContent'
>>> os.path.basename('G:\\python\\pycharmContent\\tmp')
'tmp'
>>> os.getcwd().split('\\')
['G:', 'python', 'pycharmContent', 'tmp']
>>> os.path.split('G:\\python\\pycharmContent\\tmp')
('G:\\python\\pycharmContent', 'tmp')
# 路径拼接
>>> os.path.join('G:\\python\\pycharmContent', 'tmp')
'G:\\python\\pycharmContent\\tmp'
>>> '\\'.join(p)
'G:\\python\\pycharmContent\\tmp'
# 判断类型
>>> os.path.isdir('tmp')  # 存在且为目录？
True
>>> os.path.isfile('tmp')  # 存在且为文件？
False
>>> os.path.islink('tmp')  # 存在且为链接？
False
>>> os.path.ismount('G:\\')  # 存在且为挂载点？
True
```

## 2.pickle模块

### (1) pickle模块简介

- 把数据写入文件时，常规的文件方法只能把字符串对象写入。其他数据需要先转换成字符串再写入文件
- python提供了一个标准的模块，称之为pickle。使用它可以在一个文件中存储任何python对象，之后又可以把它无损取出

### (2) pickle模块方法

- 分别调用dump()和load()可以存储、写入

```python
>>> import pickle
>>> shopping_list = ['apple', 'banana', 'orange']
>>> with open('shop.data', 'wb') as fobj:
...     pickle.dump(shopping_list, fobj)  # 存入数据
>>> with open('shop.data', 'rb') as f:
...     mylist = pickle.load(f)  # 取出数据，依然是列表格式
...     
>>> type(mylist)
<class 'list'>
>>> mylist
['apple', 'banana', 'orange']
```

### (3) 案例：记账程序

> 1. 假设在记账时，有一万元
> 1. 无论开销还是收入都要进行记账
> 1. 记账内容包括时间、金额和说明等
> 1. 记账数据要求永久存储

| 日期       | 收入  | 支出 | 余额  | 说明   |
| ---------- | ----- | ---- | ----- | ------ |
| 2019-07-08 | 0     | 0    | 10000 | init   |
| 2019-07-09 | 10000 | 0    | 20000 | salary |
| 2019-07-09 | 0     | 200  | 19800 | eat    |

```python
# 数据保存的形式
# 用列表存储数据，第一行是列表中的一项，列表中的每一项也是列表
# 小列表中的每一项是各个字段
[
    ['2019-07-08', 0, 0, 10000, 'init'],
    ['2019-07-09', 10000, 0, 20000, 'salary'],   
]
```

```python
import time
import os
import pickle


def save(fname):
    print('save'.center(50, '-'))
    date = time.strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额float代替int可以有小数点
    comment = input('comment: ')  # 说明
    with open(fname, 'rb') as f:
        records = pickle.load(f)
    balance = records[-1][-2] + amount  # 余额
    new_record = [date, amount, 0, balance, comment]
    records.append(new_record)  # 列表追加
    # 将更新后的列表写入文件
    with open(fname, 'wb') as f:
        pickle.dump(records, f)


def cost(fname):
    print('cost'.center(50, '-'))
    date = time.strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额float代替int可以有小数点
    comment = input('comment: ')  # 说明
    with open(fname, 'rb') as f:
        records = pickle.load(f)
    balance = records[-1][-2] - amount  # 余额
    new_record = [date, 0, amount, balance, comment]
    records.append(new_record)  # 列表追加
    # 将更新后的列表写入文件
    with open(fname, 'wb') as f:
        pickle.dump(records, f)


def query(fname):
    print('query'.center(50, '-'))
    # 打印表头
    print('%-12s%-8s%-8s%-12s%-15s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(fname, 'rb') as f:
        records = pickle.load(f)

    for line in records:
        print('%-12s%-8s%-8s%-12s%-15s' % tuple(line))

def show_menu():
    # 初始化数据
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Input your choice(0/1/2/3): """
    fname = 'record.data'
    init_data = [
        ['2019-07-09', 0, 0, 10000, 'init']
    ]
    # 没有record.data文件，则创建
    if not os.path.exists(fname):
        with open(fname, 'wb') as f:
            pickle.dump(init_data, f)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice, try again.')
            continue

        if choice == '3':
            print('\nBye')
            break

        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
```

