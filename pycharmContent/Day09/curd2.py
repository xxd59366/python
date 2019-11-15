from dbconn import Employees, DBSession

# 创建会话实例,用于连接数据库
session = DBSession()

# 创建员工实例
zs = Employees(
    emp_id=1,
    emp_name='张三',
    birth_date='1990-05-28',
    email='zd@qq.com',
    dep_id=2
)
ls = Employees(
    emp_id=2,
    emp_name='李四',
    birth_date='1898-06-18',
    email='ls@163.com',
    dep_id=1
)
w2 = Employees(
    emp_id=3,
    emp_name='李四',
    birth_date='1994-11-11',
    email='w2@qq.com',
    dep_id=3
)


# 在数据库中创建记录
emps = [zs, ls, w2]
session.add_all(emps)
session.commit()  # 确认至数据库

# 关闭会话
session.close()