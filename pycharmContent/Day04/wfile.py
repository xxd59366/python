import os


def get_fname():
    """用于获取文件名"""
    while True:
        fname = input('请输入文件名：')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')
    return fname


def get_content():
    """用于获取文件内容"""
    content = []
    print('请输入内容，end表示结束')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        line += '\n'
        content.append(line)
    return content


def wfile(fname, content):
    """将内容写入文件"""
    with open(fname, 'w') as f:
        f.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
