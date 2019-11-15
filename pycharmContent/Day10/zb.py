import os
import time

print('Starting...')
retval = os.fork()
if retval:
    print('father')
    time.sleep(10)
    print('go on')
    # os.waitpid(-1, 0)  # 挂起父进程
    os.waitpid(-1, 1)  # 不挂起父进程
    time.sleep(5)
else:
    print('son')
    time.sleep(15)
    exit()

print('Done')
