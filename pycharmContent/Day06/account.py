import time
import os
import pickle


def save(fname):
    print('save'.center(50, '-'))
    date = time.strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额float代替int可以有小数点
    comment = input('comment: ')  # 说明
    with open(fname, 'rb') as f:
        records = pickle.load(f)
    balance = records[-1][-2] + amount  # 余额
    new_record = [date, amount, 0, balance, comment]
    records.append(new_record)  # 列表追加
    # 将更新后的列表写入文件
    with open(fname, 'wb') as f:
        pickle.dump(records, f)


def cost(fname):
    print('cost'.center(50, '-'))
    date = time.strftime('%Y-%m-%d')  # 日期
    amount = int(input('amount: '))  # 金额float代替int可以有小数点
    comment = input('comment: ')  # 说明
    with open(fname, 'rb') as f:
        records = pickle.load(f)
    balance = records[-1][-2] - amount  # 余额
    new_record = [date, 0, amount, balance, comment]
    records.append(new_record)  # 列表追加
    # 将更新后的列表写入文件
    with open(fname, 'wb') as f:
        pickle.dump(records, f)


def query(fname):
    print('query'.center(50, '-'))
    # 打印表头
    print('%-12s%-8s%-8s%-12s%-15s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(fname, 'rb') as f:
        records = pickle.load(f)

    for line in records:
        print('%-12s%-8s%-8s%-12s%-15s' % tuple(line))

def show_menu():
    # 初始化数据
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Input your choice(0/1/2/3): """
    fname = 'record.data'
    init_data = [
        ['2019-07-09', 0, 0, 10000, 'init']
    ]
    # 没有record.data文件，则创建
    if not os.path.exists(fname):
        with open(fname, 'wb') as f:
            pickle.dump(init_data, f)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice, try again.')
            continue

        if choice == '3':
            print('\nBye')
            break

        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
