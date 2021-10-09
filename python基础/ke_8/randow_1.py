import random  # 引入随机模块

#
# r1 = random.randint(1, 6)
# r2 = random.uniform(1, 6)
# r3 = random.choice([324, 432, 4, 32, 4, 32, 432, 4])  # 在一个序列中随机获取一个值
# r4 = random.random()  # 生成0-1随机浮点数
# print(r4)

# 抽奖程度：一等将 笔记本电脑0.001    二等奖 冰箱 0.01 三等奖 音响 0.05    谢谢回顾   1-0.001-0.01-0.01
print("正在抽奖。。。。。。。。。。。")

r1 = random.randint(1, 1000)
print("您的抽奖号码是", r1)
if r1 == 1:
    print("*** 运气非常好，获得一等奖，笔记本电脑 ***", r1)
elif 10 <= r1 <= 19:
    print("*** 恭喜您，获得二等奖，冰箱 ***", r1)
elif 100 <= r1 < 149:
    print("*** 恭喜您，获得三等奖，音响 ***", r1)
else:
    print("*** 谢谢惠顾！***")
