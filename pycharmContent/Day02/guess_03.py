import random

# 随机取出100以内的整数，包括1和100
num = random.randint(1, 100)
prompt = "'-' * 20 + '猜数字游戏' + '-' * 20"
counter = 0

while counter < 5:
    x = input('请输入1-100的数字:\n')
    if x == '':
        prompt = '请输入！'
        print(prompt)
    else:
        gamer = int(x)
        if 1 <= gamer <= 100:
            if gamer == num:
                prompt = '恭喜猜对了!'
                print(prompt)
                break
            else:
                counter += 1
                prompt = '猜大了！' if gamer > num else '猜小了'
                print(prompt)
        else:
            prompt = '输入不合法!'
            print(prompt)
else:
    print('正确值为 %s' % num)

# 使用while的else格式，只有在break不触发时，else才会执行