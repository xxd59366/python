# data会占用大量的内存
with open('/bin/ls', 'rb') as f1:
    data = f1.read()

with open('/root/ls', 'wb') as f2:
    f2.write(data)