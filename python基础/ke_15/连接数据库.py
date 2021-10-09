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
dt = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)

dt.close()  # 关闭数据库连接
