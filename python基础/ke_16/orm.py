# ���ݿ����
import pymysql

host = "localhost"
port = 3306
user = "root"
password = "123456"
db = "51db"
charset = "utf8"


# �������ݿ�,�������Ӷ���
def getConnection():
    db = pymysql.connect(host=host, port=port, user=user, passwd=password, charset=charset)
    return db


# ��ѯ����
def getData(sql):
    db = getConnection()
    cursor = db.cursor()
    data = None  # ���淵�ص�����
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print("�쳣:", e)
    finally:
        cursor.close()
        db.close()
    return data


# ��������
def writeData(sql):
    db = getConnection()
    cursor = db.cursor()

    try:
        r = cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
        print("------�����Ѹ���-------",r)
    except Exception as e:
        print("�쳣:", e)
    finally:
        cursor.close()
        db.close()
