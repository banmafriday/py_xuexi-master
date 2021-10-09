# json模拟数据库
# 在文本文件中保存json字符,通过文件读写来操作数据
import json

#
# # 只创建文本文件
# with open(r"user.txt", "w")as f:
#     users = '[{"uname":"zhangshan","upwd":"123","uname":"lisi","upwd":"123","uname":"wangwu","upwd":"123"}]'
#
#     f.write(users)

# 读取数据 (查询)
def readData():
    with open(r"user.txt", "r")as f:
        jsonData = f.read()
    userList = json.loads(jsonData)
    return userList


# 写数据(修改)
def writeData(userList):
    jsonData = json.dumps(userList, ensure_ascii=False)
    with open(r"user.txt", "w")as f:
        f.write(jsonData)
        print("数据写入成功")
    userList = json.loads(jsonData)
    return userList


# 注册(在数据库增加用户)
def reg():
    name = input("请输入新用户名:")

    password = input("请输入密码")
    newuser = {"uname": name, "upwd": password}  # 新用户
    userList = readData()
    userList.append(newuser)  # 将新用户添加用户列表
    writeData(userList)
    print("新用户添加成功")


# 登录
def login():
    name = input("请输入用户名:")

    password = input("请输入密码")
    userList = readData()  # 读取所有用户列表
    msg = "失败"
    for user in userList:
        print(user)
        if name == user["uname"] and password == user["upwd"]:
            msg = "成功"
            print("登录成功")

        if msg == "失败":
            print("登录失败")
        return msg


if __name__ == '__main__':
    login()
