# coding:utf-8
import pymysql

# 创建数据库
host = "localhost"
port = 3306
user = "root"
password = "123456"
db = "51db"
charset = "utf8"
# 创建连接对象,并且建立连接
db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
print("数据库")
# 创建游标对象
curses = db.cursor()

# 创建表
for i in range(1,20):
    sql = "insert into python(id,name,age) values (1,2,25)"


    # 执行sql
    curses.execute(sql)

    # 提交数据
    db.commit()

# 关闭游标
curses.close()
db.close()  # 关闭数据库连接
