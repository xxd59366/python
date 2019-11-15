import os

print('Starting...')
retval = os.fork()
if retval:  # 父进程的retval非零
    print('in partent')
else:
    print('in child')
print('Hello World!')

