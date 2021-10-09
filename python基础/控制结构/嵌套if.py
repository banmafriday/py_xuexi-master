# if 选择结构嵌套
# if
money = int(input("请输入存款金额(万)"))
day = int(input("今天星期几(1-7)"))
banma = int(input("有没有钱?"))
if money>=100:
    print("恭喜你!可以买宝马了")

    if day <= 5:
        print("周末去")
        if banma == 1:
            print("正确")
        else:
            print("错误")
    else:
        print("今天去")
elif money>=50 and money<100:
    print("买丰田")
elif money>=20 and money<50:
    print("买二手车")
else:
    print("单车")
