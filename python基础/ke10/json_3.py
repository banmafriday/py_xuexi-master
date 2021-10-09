import json
import datetime
import time


# 写入初始数据
# d = '[{"时间": "2021/10/1 19:22", "项目": "收到王敏货款", "金额": 3000, "分类": "收入",' \
#     '"时间": "2021/10/2 19:22", "项目": "吃饭", "金额": 23, "分类": "支出",' \
#     '"时间": "2021/10/3 19:22", "项目": "买手机", "金额": 2000, "分类": "支出"}]'
#
# with open(r"data.txt", "w")as f:
#     f.write(d)


# 读json数据
def readData():
    with open(r"data.txt", "r") as f:
        jsonData = f.read()
    dataList = json.loads(jsonData)
    return dataList


# 写json数据
def writeData(dataList):
    jsondata = json.dumps(dataList, ensure_ascii=False)
    with open(r"data.txt", "w") as f:
        f.write(jsondata)
        print("-----数据写入成功-----")


# 显示账目
def showData():
    sumIn = 0
    sunOut = 0
    dataList = readData()
    print("******************************************")
    for data in dataList:
        if data["分类"] == "支出":
            sunOut += data["金额"]

            print(data["时间"], "  ", data["项目"], "   ", data["金额"] * -1)
        else:
            sumIn += data["金额"]
            print(data["时间"], "  ", data["项目"], "   ", data["金额"])
    print("**总收:", sumIn, "元", "总开支:", sunOut, "元", sumIn - sunOut, "元!")

    print("******************************************")


# 增加一笔账目
def addData():
    dataList = readData()
    content = input("请输入明细:")
    aomount = float(input("请输入金额:"))
    c = int(input("请输入分类:1.收入,2支出"))
    cla = "支出"
    if c == 1:
        cla = "收入"
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    newData = {"时间": t, "项目": content, "金额": aomount, "分类": cla}

    dataList.append(newData)
    writeData(dataList)


if __name__ == "__main__":
    while 1 == 1:

        showData()
        c = int(input("增加账目请输入1:"))
        if c == 1:
            addData()
        time.sleep(2)
        print("\n\n\n")
