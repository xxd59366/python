import sys
import hashlib


def md5check(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


if __name__ == '__main__':
    fname = sys.argv[1]
    result = md5check(fname)
    print(result)
