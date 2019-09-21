import random
import string


def passinit():
    mystr = string.ascii_letters+string.digits
    p = ''
    n = int(input('生成密码的位数：'))
    for i in range(n):
        p += random.choice(mystr)

    print('Your pass is %s' % p)


if __name__ == '__main__':
    passinit()
