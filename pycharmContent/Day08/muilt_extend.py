class A:
    def func1(self):
        print('func1 A')

    def func3(self):
        print('func3 A')


class B:
    def func2(self):
        print('func2 B')

    def func3(self):
        print('func3 B')


class C(A, B):
    # def func3(self):
    #     print('func3 C')
    pass


if __name__ == '__main__':
    c = C()
    c.func1()
    c.func2()
    c.func3()
