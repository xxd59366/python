import sys
import random
import subprocess
import string

all_chs = string.digits + string.ascii_letters


def gen_pass(n=8):
    # 生成密码
    str_list = [random.choice(all_chs) for i in range(n)]
    return ''.join(str_list)


def add_user(uname, upass, fname):
    # 判断文件是否存在
    isex = subprocess.run(
        'id %s' % uname, shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if isex.returncode == 0:
        return 'error：user %s already exists!' % uname

    # 创建用户
    cr_usr = subprocess.run('useradd %s' % uname, shell=True)
    ch_pw = subprocess.run(
        'echo %s | passwd --stdin %s' % (upass, uname),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # 将信息写入文件
    info = """用户信息：
用户名：%s
密码：%s

""" % (uname, upass)
    with open(fname, 'a') as f:
        f.write(info)
        return 'success'


if __name__ == '__main__':
    uname = sys.argv[1]
    upass = gen_pass()
    fname = '/tmp/users.txt'
    rs = add_user(uname, upass, fname)
    print(rs)
