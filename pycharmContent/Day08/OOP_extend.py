class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print("I'm %s.%s" % (self.name, words))

    def run(self):
        print('%s is running...' % self.name)


class Warrior(Role):
    def __init__(self, name, gender, weapon):
        # 下面两种写法是等价的
        # Role.__init__(self, name, weapon)
        super(Warrior, self).__init__(name, weapon)
        self.gender = gender


if __name__ == '__main__':
    gy = Warrior('关羽', '男', '青龙偃月刀')
    gy.speak('我不是针对谁,我是说在座的各位都是辣鸡.')
    gy.run()
