src_fname = '/bin/ls'
dst_fname = '/tmp/list'

src_f = open(src_fname, 'rb')
dst_f = open(dst_fname, 'wb')

while True:
    data = src_f.read(4096)
    if not data:
        break
    else:
        dst_f.write(data)

src_f.close()
dst_f.close()