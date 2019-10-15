import random


def num_todo():
    num = [random.randint(1, 100) for i in range(2)]
    num.sort(reverse=True)  # 降序排列
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    wtdo = random.choice('+-')
    result = cmds[wtdo](*num)
    return num, wtdo, result


def show_menu():
    num, wtdo, result = num_todo()
    prompt = """%s%s%s=: """ % (num[0], wtdo, num[1])
    count = 0

    while True:
        count += 1
        try:
            guess = int(input(prompt).strip())
        except (EOFError, KeyboardInterrupt):
            print('exit')
            exit(1)
        except Exception:
            print('Invalid Value')
            exit(2)
        if guess == result:
            print('you are right ~~^_^~~')
            try:
                while True:
                    ch = input('Continue?(y/n) ')
                    if ch not in ['y', 'n']:
                        print('Invalid input!')
                        continue
                    if ch == 'y':
                        show_menu()
                    break
            except:
                pass
            print('Bye')
            break


        if count == 3:
            print('Your chances have used up.The result is %s' % result)
            break

        print('Not right. try again please. You have %s chance yet.' % (3 - count))
        continue


if __name__ == '__main__':
    show_menu()
