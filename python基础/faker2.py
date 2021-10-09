# coding:utf-8
import pymysql
from faker import Faker

faker = Faker("zh_CN")  # 中文数据


def insert_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='sys',
                           charset='utf8mb4')
    cursor = conn.cursor()
    # SQL 插入语句
    sql = "UPDATE xiaozu_phonecode set id='150' WHERE id >1"
    person_data = []

    for i in range(110000):
        a = 1
        a += 1
        print(i,i)
        person_data.append(i)

    print(person_data)
    try:
        # 执行sql语句
        cursor.executemany(sql, person_data)  # todo 批量生成数据用executemany
        # 提交到数据库执行
        conn.commit()
        print("插入数据完成...")
    except Exception as e:
        # 如果发生错误则回滚
        conn.rollback()
        raise e
    finally:
        conn.close()  # 关闭数据库连接


insert_data()
