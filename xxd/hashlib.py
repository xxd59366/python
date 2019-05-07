import hashlib
import sys

def check_md5(fname):
    with open(fname,'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

print(check_md5(sys.argv[1]))
