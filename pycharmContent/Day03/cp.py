# 复制文件
src = open('/bin/ls','rb')
dst = open('/root/ls','wb')
data = src.read()
dst.write(data)
dst.close()
src.close()
