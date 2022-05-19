#!/bin/python3
import time
import os
import tarfile
import hashlib
import pickle
import sys


# MD5校验
def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


# 完全备份
def full_backup(src_dir, fname, md5file):
    md5dict = {}

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


# 增量备份
def incr_backup(src_dir, dst_dir, md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    md5dict = {}

    with open(md5file, 'rb') as fobj:
        oldmd5 = pickle.load(fobj)

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if oldmd5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    # 拉路径
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    # 子路径生成
    mon = time.strftime('%m')
    dst_dir = os.path.join(dst_dir.rstrip('/'), mon)
    # 检查是否已有备份，如果没有，则完全备份
    # 因为每天执行一次，如果月份出现变化，检测不到目录，则完全备份
    md5file = os.path.join(dst_dir, 'md5.data')
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
        fname = os.path.basename(src_dir.rstrip('/'))
        fname = '%s_full_%s.tar.gz' % (fname, time.strftime('%Y%m%d'))
        fname = os.path.join(dst_dir, fname)
        full_backup(src_dir, fname, md5file)
        exit(0)
    else:
        # 月份不出现变化且目录存在时，执行增量备份
        incr_backup(src_dir, dst_dir, md5file)
