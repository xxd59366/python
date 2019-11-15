class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """显示实例时自动调用"""
        return '《%s》' % self.title

    def __call__(self, *args, **kwargs):
        print('《%s》为%s编著' % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('python核心编程', '韦斯利') # 调用init
    print(core_py)
    core_py()