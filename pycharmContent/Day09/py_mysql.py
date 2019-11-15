import pymysql

# 创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1902',
    charset='utf8'
)

# 创建游标,用来执行SQL语句
cursor = conn.cursor()

# 编写需要执行的SQL语句
create_dep = '''Create Table department(
dep_id INT,
dep_name VARCHAR(20),
Primary Key(dep_id)
)'''
create_emp = '''Create Table employees(
emp_id INT,
emp_name VARCHAR(20),
birth_date DATE,
phone VARCHAR(11),
email VARCHAR(50),
dep_id INT,
Primary Key(emp_id),
Foreign Key(dep_id) References departments(dep_id)
)'''
create_sal = '''Create Table salary(
id INT,
date DATE,
emp_id INT,
basic INT,
awards INT,
Primary Key(id),
Foreign Key(emp_id) References employees(emp_id)
)'''

# 执行SQL语句
cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)

# 确认
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
