## 常用配置

```shell
set et
set ci
set sw=4
set ts=4
```

### 配置解析

#### 1.set ts=4

· 等于set tabstop=4

· 在使用vim编辑器的时候  很多系统里默认的vim tapstop是8，而很多时候我们需要的tapstop是4，比如在写python的时候，我们都知道python严重依赖缩进，所以tapstop是8的话 ，这个脚本比较大的时候那就相当的不好看了，所以在这种情况下修改tapstop为4还是很有必要的

· 但是问题又来了，在python脚本里，如果缩进使用tab那么就不再推荐在同一脚本里使用其他的符号来缩进，因为这很有可能导致诸多兼容性问题，比如你既使用了tab又在某些地方使用了空格来缩进，额，恭喜你，你很有可能会遇到无法执行此脚本的错误。

· 这个时候怎么办呢？最显而易见的方法只有一个，那就是统一使用相同的缩进方法，该是做出艰难的选择的时候了：要么用tab  要么用空格 。而很多经常使用python的同学可能会发现使用空格缩进比tab来缩进似乎更加明智，因此也极力推荐统一使用空格，这是为什么呢？当你vim编辑一个文件的时候，你能一眼就看出缩进使用的是tab吗？最有可能发生的是把tab当成了空格而不是把空格看成tab。为了避免这样的困扰，统一使用空格看起来是更好的选择。

#### 2.set et

· 等同于set expandtab

· 打开vim，按下tab，再按backspace，你会发现tab出来的缩进只需要backspace一次就能删除，这足以说明这段空白是tab，加入set et后

· 再次打开vim，你会发现tab出来的空白已经变成空格了，而这个时候一个tab就真正成为4个空格了，而不仅仅是4个空格的缩进距离，这才是我们真正想要的。

· 如果你编辑了一个文件并且想要在别人修改这个文件的时候不会出现类似的疑问怎么办呢？方法有两个，一个是你告诉他，你使用的是空格还是tab，另一个方法是使用vim的modeline，当别人打开这个文件的时候会自动使用相同的配置。

· 我们可以在文件末尾添加行：

```shell
# vim:et:ts=4:sw=4:
```

这个就是modeline，当其他人的vimrc里打开了set modeline的时候，就会自动读入此配置。

## 打造vim为python IDE

### (1) 创建vim插件工作目录

```shell
# mkdir -p ~/.vim/bundle/
```

### (2) 下载插件

```shell
# cd ~/.vim/bundle/
# git clone https://github.com/rkulla/pydiction.git
# ls
pydiction
```

### (3) 将pydiction目录中的after目录拷贝到~/.vim/目录。当执行vim时，会自动执行 \~/.vim/目录中的内容

```shell
# cp -r pydiction/after/ ~/.vim/
```

### (4) 修改vim配置，设置打开以.py结尾的文件，按tab可以支持python语法补全

```shell
# vim ~/.vimrc
let g:pydiction_location = '~/.vim/bundle/pydiction/complete-dict'
set ai
set et
set ts=4
```

### (5) 测试：只能补全以.py结尾的文件

```shell
# vim test.py
imp<tab>
```

