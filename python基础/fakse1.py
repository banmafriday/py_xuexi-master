# coding:utf-8
import pymysql
from faker import Faker
import time

faker = Faker("zh_CN")  # 中文数据


def insert_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='sys',
                           charset='utf8mb4')
    cursor = conn.cursor()
    # SQL 插入语句
    sql = "INSERT INTO xiaozu_phonecode(id,phone,type,addtime,code,name,ssn,job,address,url,ascii_email,date,sentence,random_digit_not_null," \
          "phone_number,credit_card_number,pystr)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    person_data = []
    for i in range(1000000):
        person_info = (
            faker.phonenumber_prefix(), faker.phone_number(), faker.ean8(), faker.ean8(), faker.ean8(), faker.name(),
            faker.ssn(), faker.job(), faker.address(), faker.url(), faker.ascii_email(), faker.date(),
            faker.sentence(), faker.random_digit_not_null(), faker.phone_number(), faker.credit_card_number(),
            faker.pystr())
        person_data.append(person_info)

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
