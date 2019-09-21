import functools


def foo(a, b, c, d, e):
    return a + b + c + d + e


add = functools.partial(foo, a=1, b=2, c=3, d=4)
add1 = functools.partial(foo, *[1, 2, 3, 4])
add2 = functools.partial(foo, **{'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(add(e=5))
print(add1(5))
print(add2(e=5))
