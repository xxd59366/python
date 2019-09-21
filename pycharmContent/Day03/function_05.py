# 拷贝脚本修改
import sys


def cp_func(src_name, dst_name):
    with open(src_name, 'rb') as src_f:
        with open(dst_name, 'wb') as dst_f:
            while True:
                data = src_f.read(4096)
                if not data:
                    break
                else:
                    dst_f.write(data)


cp_func(sys.argv[1], sys.argv[2])
