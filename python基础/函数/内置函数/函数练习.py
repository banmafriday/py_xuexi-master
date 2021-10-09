# # 1.写函数,接收3个数字参数,返回最大的那个数字。
#
# def getMax(a, b, c):
#     r = max([a, b, c])
#     return r
#
#
# s = getMax(24, 43, 433)
# print(s)


# # 2.编写一个用户登录函数(用户名密码提前设置);
# # #返回用户登录成功或者失败的结果;
#
# name = "aaa"
# paaword = "123"
#
#
# def login():
#     msg = "失败"
#     uname = input("请输入用户名")
#     upassword = input("请输入密码")
#     if name == uname and paaword == upassword:
#
#         msg = "成功"
#     else:
#         print("登录失败")
#     return msg
#
#
# r = login()
# print(r)


# 3.做一个分数统计器︰

# 函数中让用户循环输入一组分数，输入结束后保存到一个列表中。
# #把平均分,最高分,最低分，及格人数,及格率返回出来。

def getData():
    avgScore = 0
    maxavgScore = 0
    minavgScore = 0
    passCount = 0
    passPre = 0
    scoreList = []

    while 1 == 1:
        st = int(input("请输入一个分数"))
        scoreList.append(st)
        if st >= 60:
            passCount += 1
        c = int(input("结束请按1,继续请按2"))
        if c == 1:
            break
    av = sum(scoreList) / len(scoreList)
    maxc = max(scoreList)
    mins = min(scoreList)
    passp = passCount / len(scoreList)
    return avgScore, maxavgScore, minavgScore, passCount, passPre


avgScore, maxavgScore, minavgScore, passCount, passPre = getData()
print(avgScore, maxavgScore, minavgScore, passCount, passPre)