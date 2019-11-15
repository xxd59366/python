class Weapon:
    def __init__(self, wname, strength):
        self.wname = wname
        self.strength = strength


class Warrior:
    def __init__(self, name, weapon):
        """实例化时自动调用"""
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print(r"I'm %s, %s" % (self.name, words))

    def show_me(self):
        print("我是%s, 我是一个战士, 我的武器是%s" % (self.name, self.weapon.wname))


if __name__ == '__main__':
    blade = Weapon('青龙偃月刀', 100)
    gy = Warrior('关羽', blade)
    gy.speak('过五关斩六将')
    gy.show_me()

    cz = Weapon('禅杖', 100)
    lzs = Warrior('鲁智深', cz)
    lzs.show_me()
    print('%s用的是%s, 伤害为%s' % (lzs.name, lzs.weapon.wname, lzs.weapon.strength))
