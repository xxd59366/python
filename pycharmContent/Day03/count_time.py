import time


def count_time(func):
    start_time = time.time()

    def ct():
        func()
        end_time = time.time()
        return end_time - start_time

    return ct


@count_time
def func1():
    time.sleep(1)


@count_time
def func2():
    time.sleep(2)


if __name__ == '__main__':
    print(count_time(func1)())
    print(count_time(func2)())
    print()
    print(count_time(func2)())
    print(func2())
