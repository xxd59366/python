import subprocess
import sys


def subr(com, args):
    for i in args:
        print('\033[031;1m%s %s\033[0m' % (com, i))
        subprocess.run(com+' '+i, shell=True)


if __name__ == '__main__':
    print(sys.argv)
    com = sys.argv[1]
    for i in range(2):
        sys.argv.remove(sys.argv[0])
    args = sys.argv
    # print(args)
    subr(com, args)
