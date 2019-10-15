import shutil
import os  # 删除单个文件需要导入 os 模块


def cpfobj(src, dst):
    # copyfile值了解底层原理，实际代码不需要使用
    f1 = open(src, 'rb')
    f2 = open(dst, 'wb')
    shutil.copyfileobj(f1, f2)
    f1.close()
    f2.close()


def cpf(src, dst):
    # 只拷贝内容
    shutil.copyfile(src, dst)


def cp(src, dst):
    # 既拷贝内容，又拷贝权限
    shutil.copy(src, dst)


def cp2(src, dst):
    # 相当于cp -p
    shutil.copy2(src, dst)


def mv(src, dst):
    # 相当于mv
    shutil.move(src, dst)


def cptr(src, dst):
    # 需要将目标名也写出来
    shutil.copytree(src, dst)


def rmtr(path):
    # 相当于rm -rf，但只能删除目录
    shutil.rmtree(path)


def rm(path):
    # 删除单个文件
    os.remove(path)


if __name__ == '__main__':
    cpfobj('/bin/ls', '/tmp/list5')
    cpf('/bin/ls', '/tmp/list6')
    cp('/bin/ls', '/tmp/list7')
    cp2('/bin/ls', '/tmp/list8')
    mv('/tmp/list8', '/tmp/list')
    cptr('/etc/security', '/tmp/security')
    mv('/tmp/security', '/var/tmp/auquan')
    rmtr('/var/tmp/auquan')
    rm('/tmp/list5')
