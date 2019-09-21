src_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(src_fname, 'rb') as src_f:
    with open(dst_fname, 'wb') as dst_f:
        while True:
            data = src_f.read(4096)
            if not data:
                break
            else:
                dst_f.write(data)