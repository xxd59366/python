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
    cmds = {0: in_stack, 1: out_stack, 2:search}
    # 用字典调用函数可以提高效率
    if ch in [0, 1, 2]:
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
    # print(stack)
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
