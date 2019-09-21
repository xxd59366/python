# python交互解释器tab补全功能

### (1) 创建指令补全文件

```shell
# vim /usr/local/bin/tab.py
from rlcompleter import readline

readline.parse_and_bind('tab: complete')
```



### (2) 配置环境变量，在~/.bashrc中追加以下内容

```shell
# vim ~/.bashrc
export PYTHONSTARTUP='/usr/local/bin/tab.py'
```

### (3) source生效

```shell
# source ~/.bashrc
```

### (4)  进入python解释器

```shell
# python3
>>> pr<tab><tab>
>>> pri<tab>
```