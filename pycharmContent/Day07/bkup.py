import os
from time import strftime


def full_backup():
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    pass


def incr_backup():
    pass


if __name__ == '__main__':
    src = r'G:\python\pycharmContent\Day07\demo'
    dst = r'G:\python\pycharmContent\Day07\backup'
    md5file = r'G:\python\pycharmContent\Day07\backup\md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)

