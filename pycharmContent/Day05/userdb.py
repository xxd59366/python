import getpass
userdb = {}

def register():
    print('register'.center(50, '-'))
    uname = input('username: ')
    if uname in userdb:
        print('\033[31;1musername already exists, try again.\033[0m')
    else:
        pw = input('password: ')
        userdb[uname] = pw

def login():
    print('login'.center(50, '-'))
    uname = input('username: ')
    pw = getpass.getpass('password: ')
    if userdb.get(uname) == pw:
        print('\033[32;1msuccess!\033[0m')
    else:
        print('\033[31;1minvalid login!\033[0m')


def show_menu():
    prompt = """(0) 退出
(1) 注册
(2) 登录
"""
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('invalid input, try again please!')
            continue

        if choice == '0':
            print('Bye!')
            break

        cmds = {'1': register, '2': login}
        cmds[choice]()

if __name__ == '__main__':
    show_menu()