from dbconn import Departments, Employees, DBSession

# 创建会话实例,用于连接数据库
session = DBSession()

# 查询数据库,返回实体类的实例
qset1 = session.query(Departments)
print(qset1)  # 此时只是一条SQL语句,不真正连接数据库
print(list(qset1))  # 取值的时候,才会连接数据库
for dep in qset1:
    print('部门ID: %s, 部门名称: %s' % (dep.dep_id, dep.dep_name))
# 如果查询某些字段,返回的是元组
qset2 = session.query(Employees.emp_name, Employees.email)
print(qset2)  # qset2是SQL语句
print(list(qset2))  # 取值是元组
# 排序
qset3 = session.query(Departments).order_by(Departments.dep_id)
for dep in qset3:
    print(dep.dep_id, dep.dep_name)
# 排序,取切片
qset4 = session.query(Departments).order_by(Departments.dep_id)[2:4]
print(qset4)  # 因为qset4执行了切片取值,所以它不是sql语句了
for dep in qset4:
    print(dep.dep_id, dep.dep_name)
# 通过filter函数实现结果过滤
qset5 = session.query(Employees).filter(Employees.dep_id==2)
for emp in qset5:
    print(emp.emp_name)
# filter叠加使用
qset6 = session.query(Employees).filter(Employees.dep_id==2)\
    .filter(Employees.email.like('%163.com'))
for emp in qset6:
    print(emp.emp_name, emp.email)
# all方法返回列表, first方法返回结果的第一项
qset7 = session.query(Departments).order_by(Departments.dep_id)
print(qset7.all())
print(qset7.first())
# 实现多表查询
qset8 = session.query(Employees.emp_name, Departments.dep_name).join(Departments)
for item in qset8:
    print(item)  # 多表查询时query的第一个参数是Employees.emp_name, join时要写Departments
    # 如果query的第一个参数是Departments.dep_name, join时要写Employees
qset9 = session.query(Departments.dep_name, Employees.emp_name).join(Employees)
for item in qset9:
    print(item)

# 更新,首先找到记录对应的实例,然后对实例重新赋值就行
qset10 = session.query(Departments).filter(Departments.dep_name=='人事部')
print(qset10.all())
hr = qset10[0]  # 从列表中取出第一个元素
hr.dep_name = '人力资源部'
session.commit()  # 对数据库进行操作需要commit

# 删除操作,将7号部门删除
qset11 = session.query(Departments).filter(Departments.dep_id==7)
sales = qset11[0]
session.delete(sales)
session.commit()

# 关闭会话
session.close()
