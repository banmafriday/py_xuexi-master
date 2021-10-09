# 开发一个计算器,用户输入第一个数,加减乘除,第二个数,控制台显示计算结果
a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
s = input("请输入计算方式+-/*")
msg = 1   # 记录是否有结果  0没结果  1有结果
result  = 0 # 保持计算结果
if s == "+":
    result = a+b
elif s == "-":
    result = a-b
elif s == "*":
    result = a*b
elif s == "/":
    result = a/b
else:
    print("没有这种计算方式")
    msg=0
if msg == 1:
    print("计算结果",result)