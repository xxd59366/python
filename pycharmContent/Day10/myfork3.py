import os

print('Starting...')
for i in range(3):
    retval = os.fork()
    if not retval:
        print('Hello')
        exit()  # 子进程遇到exit后,后续代码将不再执行

print('Done')

