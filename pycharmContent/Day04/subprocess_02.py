# 捕获输出
import subprocess

rc = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(rc.returncode)
print(rc.stdout.decode(), end='')
print(rc.stderr.decode(), end='')
