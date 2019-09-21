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