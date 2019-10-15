import random
import string

mystr = string.ascii_letters + string.digits


def passinit(n=8):
    p = ''
    for i in range(n):
        p += random.choice(mystr)
    return p


if __name__ == '__main__':
    pw = passinit()
    print('Your pass is %s' % pw)
