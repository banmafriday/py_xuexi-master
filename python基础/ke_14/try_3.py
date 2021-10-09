# coding:utf-8
# 自定义异常
exp = Exception("性别只能是男或者女")  # 创建一个异常对象

sex = input("请输入您的性别(男,女)")
if sex == "男" or sex == "女":
    print("您的性别:", sex)
else:
    print("&PBiOq3PrjJj")
    raise exp
