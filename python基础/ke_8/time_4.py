import time

# # 1#打印时间戳，获取程度执行时间
# a1 = time.time()  # 获取一个时间戳
# for i in range(1, 10001):
#     print(i)
# a2 = time.time()
# print(a2 - a1)


# 2获取当前本地日期和时间
t = time.localtime()
print(t)

# 将日期和时间转换成指定格式的字符串
as1 = time.strftime("%Y年-%m月-%d日----%H:%M:%S", t)
print(as1)

# # 程序休眠 10秒
# time.sleep(10)
# print("hello")

# # 程序休眠 5小时
# time.sleep(5 * 60 * 60)
# print("hello")

# 倒计时
i = 10
while i >= 0:
    print("倒计时：",i)
    i-=1