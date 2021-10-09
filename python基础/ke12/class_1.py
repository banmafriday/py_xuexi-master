# 创建类
# coding:utf-8

class Cat:

    # 初始化方法
    def __init__(self, nick, clor, age):
        # 属性:昵称,颜色,年龄
        self.nick = nick
        self.clor = clor
        self.age = age

    def eat(self):
        print(self.nick)

    def sleep(self):
        print("猫在睡觉")


# --------------------------
cat1 = Cat(nick="小小", clor="白色", age=18)
cat2 = Cat(nick="小B", clor="黑色", age=8)

# 获取对象属性
print(cat1.clor)
print(cat2.nick)

# 获取方法
cat1.nick()
