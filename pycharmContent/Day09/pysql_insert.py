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
# 向部门表中插入数据
# 编写SQL语句
# 1. 插入部门数据
insert_dep = 'Insert Into departments Values (%s, %s)'
# 填写每个部门的字段值
hr = (1, '人事部')
ops = (2, '运维部')
dev = (3, '开发部')
qa = (4, '测试部')
market = (5, '市场部')
deps = [ops, dev, qa]
# 执行sql语句
cursor.execute(insert_dep, hr)  # 插入一条数据
cursor.executemany(insert_dep, deps)  # 插入多条数据
cursor.executemany(insert_dep, [market])  # 用列表的方式插入一条数据

# 2. 删除市场部
del_dep = 'Delete From departments Where dep_name=%s'
cursor.execute(del_dep, ('市场部',))

# 3.修改
update_dep = 'Update departments Set dep_name=%s Where dep_name=%s'
cursor.execute(update_dep, ('人力资源部', '人事部'))

# 确认
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
