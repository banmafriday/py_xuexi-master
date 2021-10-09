# 案例1
# 为一家超市开发一个简易的收银系统(以3-5种商品为例):
#使用变量保存︰商品编号商品价格商品名字
#1.提示用户输入商品编号和数量,然后显示总价多少钱。
#2.提示用广输入付款金额,然后显示找零金额。


bian1 = "1"
name1 = "苹果"
jia1 = 7

bian2 = "2"
name2 = "香蕉"
jia2 = 7

bian3 = "3"
name3 = "梨子"
jia3 = 7

bianhao = input("请输入商品编号")
shuliang = int(input("请输入商品数量"))

jia = 0
name = ""

if bianhao == bian1:
    jia = jia1
    name = name1


elif bianhao == bian2:
    jia = jia2
    name = name2
elif bianhao == bian3:
    jia = jia3
    name = name3
else:
    print("没有这种商品")

result = shuliang*jia

if result >0:
    print("您当前购买的商品是:",name, "单价:",jia,"数量",shuliang,"金额为",result)

    fu = float(input("请付钱:"))
    if fu == result:
        print("刚刚好")
    elif fu <result:
        su = result - fu
        print("钱不够还需要付",su)

    elif fu>result:
        print(fu-result)
