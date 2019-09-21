import random
print('-' * 20 + '这是一个猜拳游戏' + '-' * 20)
all_choices = ['石头', '剪刀', '布']
robot = random.choice(all_choices)
player = input('石头/剪刀/布：')
win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]

if player in all_choices:
    print('电脑出的是 %s' % (robot))
    if player.__eq__(robot):
        print('平局！')
    elif [player, robot] in win_list:
        print('\033[32;1m你赢了！\033[0m')
    else:
        print('\033[31;1m你输了！\033[0m')
else:
    print('输入不合法！')