# 使用位置参数
str01='{} is {}'.format('bob', 15)
str02='{1} is {0}'.format(15, 'bob')

# 使用关键字参数
str03='name is {name},age is {age}'.format(name='bob',age=23)
str04='姓名：{name} ,年龄：{age}'.format(**{'name': 'bob', 'age': 23})
str05='姓名：{0[name]} ,年龄：{1[age]}'.format({'name': 'bob', 'age': 23},{'age':24})

# 填充与格式化
# {:[填充字符][对齐方式：<表示左对齐，>表示右对齐][宽度]}
str06='{:<10} is {:<8}'.format('bob', 15)
str07='{:<10} is {:0>8}'.format('bob', 15)

# 使用索引
str08='姓名：{0[0]},年龄：{0[1]}'.format(['bob',23])

s=[str01,str02,str03,str04,str05,str06,str07,str08]
for i in range(len(s)):
    print(i,end=' ')
    print(s[i])
    print('index is', s.index(s[i]))
