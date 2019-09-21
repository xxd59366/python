import getpass
print('-' * 20 + '请输入用户名和密码' + '-' * 20)
uname = input('用户名：')
passwd = getpass.getpass('密码：')
if uname.__eq__('bob') and passwd.__eq__('123456'):
    print('Login successful')
else:
    print('Login incorrect')