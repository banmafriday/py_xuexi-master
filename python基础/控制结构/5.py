# 商品收银
name1 = "苹果"
jia1 = 7.3
id1 = "1"


name2 = "苹果"
jia2 = 8.8
id2 = "2"



name3 = "苹果"
jia3 = 9.6
id3 = "3"



name_result = ""
jia_result = 0

id  = input("请输入商品ID:")

shu = int(input("请输入商品的数量"))


if id == id1:
    name_result = name1
    jia_result = jia1

elif id == id2:
    name_result = name2
    jia_result = jia2
elif id == id3:
    name_result = name3
    jia_result = jia3
else:
    print("没有该商品")

j = shu*jia_result
if j>0:
    print("商品名称为",name_result,"商品数量为:",shu,"商品价格为:",j)
    fu = float(input("请付钱："))
    if fu == j:
        print("刚刚好")
    elif fu < j:
        print("钱不够，还需要付",fu - j)
    elif fu > j:
        print("找您：",fu - j)