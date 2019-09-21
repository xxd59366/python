import random
print('-' * 20 + '这是一个猜拳游戏' + '-' * 20)
result = {'pwin': 0, 'rwin': 0}
while result['pwin'] < 2 and result['rwin'] < 2:
    all_choices = ['石头', '剪刀', '布']
    robot = random.choice(all_choices)
    prompt = '''(0) 石头
(1)剪刀
(2) 布
请选择(0/1/2)'''
    index = int(input(prompt))
    player = all_choices[index]
    win_list = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]

    if player in all_choices:
        print('电脑出的是 %s' % (robot))
        if player.__eq__(robot):
            print('平局！')
        elif [player, robot] in win_list:
            print('\033[32;1m你赢了！\033[0m')
            result['pwin'] += 1
        else:
            print('\033[31;1m你输了！\033[0m')
            result['rwin'] += 1
    else:
        print('输入不合法！')
    print('比分为 \033[31;1m%s : %s\033[0m' % (result['pwin'], result['rwin']))
print('\033[31;1m游戏结束！\033[0m')