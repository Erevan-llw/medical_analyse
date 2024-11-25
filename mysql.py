import pymysql

# 1、打开数据库连接
conn = pymysql.connect(host='127.0.0.1',  # host属性
                       port=3306,  # 端口号
                       user='root',  # 用户名
                       password='123456',  # 此处填登录数据库的密码
                       db='test'  # 数据库名
                       )

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 构建插入语句
insert_query = "INSERT INTO data_table (key_column, value_column) VALUES (%s, %s)"

# 执行插入操作
for key, value in data.items():
    data_to_insert = (key, value)
    cursor.execute(insert_query, data_to_insert)

# 你可以在这里执行数据库操作，比如插入、查询等

# 关闭游标和数据库连接
cursor.close()
conn.close()
