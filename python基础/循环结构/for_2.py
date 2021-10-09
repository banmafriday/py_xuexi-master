# for循环遍历容器   遍历:将容器中的数据一个一个取出来
names = ["张三", "李四", "王五", "赵六"]

# 直接遍历

# for name in names:
#     if name == "王五":
#         print("找到了")

# 构造索引  获取所有的值
# for i in range(0,len(names)):
#     print(names[i])


#
# scores = (435,768,87,68,876,8,76,876,867,876,8,76,8,7)
# for score in scores:
#     print(score)
#
# for i in range(0,len(scores)):
#     print(scores[i])


# # 求和,并获取平均分
# total = 0
# for score in scores:
#     total = total+score
# print(total/len(scores))

# 循环遍历字典
dicta = {"name": "zhangshan", "age": "18", "play": "ball", }
for i in dicta:
    print(i, dicta[i])

# 集合
seta = {1,2,3,3,4,3,2,43,2,4,32,4,32,4}
for i in seta:
    print(i)