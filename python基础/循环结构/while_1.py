# # while
#
# i = 1
# while i <= 10:
#     print("这是第", i, "次打印hello word")
#     i = i + 1
#
# # for适合循环次数确定的业务,可以直接遍历容器
# # while 适合已知业务选好执行条件的
# year = 1
# while year <= 10:
#     print("第", year, "年,还款1.2万")
#     year = year + 1
#
# # 获取100-200之间的偶数
#
# i = 100
# while i<=200:
#     i = i+2
#     print(i)


# # for 嵌套循环
# for year in range(1, 11):
#     print("--------------第", year, "年到了-------------------------")
#     for month in range(1, 13):
#         print("!!!!!!!!!!!!!!!!!!!!!!第", month, "月,还款1000!!!!!!!!!!!!!!")
#         for sanshi in range(1, 31):
#             print("第", year, "年", month, "月", sanshi, "日", "天,还款0.03")

# 遍历多维容器
lista = [1, 234, 3, 24, 3, 24, 3, 24, 3, 24, 32, 4, 32, 4]
listb = [324, 32, 4, 32, 4, 32, 4, 43244324, 4, 32, 4, 3]
listc = [324324, 324, 3, 24, 32, 4, 32, 4, 32, 4, 32, 4, 23]
listx = [lista, listb, listc]  #二层用两个for循环

for x in listx:
    for s in x:
        print(s)

