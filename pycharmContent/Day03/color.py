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
