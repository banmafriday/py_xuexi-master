# 银行卡类
# coding:utf-8
# 封装
class Card():
    def __init__(self, cnum, cpwd, cname, cbanlannce):
        self.bankName = "python银行"
        self.cnum = cnum
        self.cpwd = cpwd
        self.cname = cname
        self.__cbanlannce = cbanlannce  # 私有属性

    def __login(self):   #私有方法
        num = input("请输入卡号:")
        pwd = input("请输入密码:")
        if num == self.cnum and pwd == self.cpwd:
            print("---恭喜你,登录成功!---")
            return "ok"
        else:
            print("验证失败")
            return "NO"

    def showBanlance(self):

        r = self.__login()  # 在类的内容调用其他 方法
        if r == "ok":
            print(self.__cbanlannce)
        else:
            print("验证失败")

    def deposit(self):

        r = self.__login()  # 在类的内容调用其他 方法
        if r == "ok":
            money = float(input("请输入存款金额:"))
            self.__cbanlannce += money
            print("存款成功,存入", money, "元!--余额", self.cbanlannce, "元")


# -------------------------------------------------------------

c1 = Card("1001", "1234", "张三", 1000)
c2 = Card("1002", "1234", "李四", 2000)
# c1.deposit()
# c2.showBanlance()

c2. __login