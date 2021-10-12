# coding:utf-8
import pymysql
import random


def getData(sql):
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
    curses.execute(sql)
    data = curses.fetchone()
    curses.close()
    db.close()
    return data


def login():
    uname = input("请输入用户名:")
    psw = input("请输入密码:")
    sql = "select * from python where id='" + uname + "' and psw='" + psw + "'"
    result = getData(sql)
    print(result)
    if result == None:
        print("失败")
    else:
        print("登录成功")


if __name__ == "__main__":
    login()
