# coding:utf-8
# 编写业务方法
import orm
import random


# 查看商品列表
def gatAllProducts():
    sql = "select * from Products;"
    data = orm.getData(sql)
    print("id     编号    名称    单价    折扣")
    for product in data:
        for i in product:
            print(i, end="    ")
        print()


# 根据编号查询商品
def getProduct():
    num = input("请输入商品编号:")
    sql = "select * from Products where num = "+ num
    data = orm.getData(sql)
    if data != None:

        print("商品名称:", data[0][1], "单价:", data[0][3], "折扣:", data[0][3])
        return data[0][1], data[0][2], data[0][3]
    else:
        print("商品不存在")
        return None


# 商品打折
def setDiscount():
    num = input("请输入要修改的商品编号:")
    discount = float(input("请输入折扣价:"))
    if 0.1 <= discount and discount <= 1:
        sql = "update Products set discount=" + str(discount) + " where num=" + num + ";"

        r = orm.writeData(sql)
        if r == 0:
            print("设置失败")
        else:
            print("商品折扣设置成功!")
    else:
        print("输入太大或太小")


# 添加商品
def addProduct():
    name = input("请输入一个商品名称:")
    num = str(random.randint(1000, 9999))
    price = input("请输入一个商品价格:")
    sql = "INSERT INTO market.products (num,name,price,discount) VALUES('" + num + "','" + name + "','" + price + "',1)"
    r = orm.writeData(sql)
    print(r)


# 根据编号删除商品
def delProduct():
    num = input("请输入商品编号:")
    sql = "delete from Products where num = " + num
    r = orm.writeData(sql)
    if r == 0:
        print("删除失败")
    else:
        print("商品", num, "删除成功!")


# 查看所有订单
def getAllOrders():
    sql = "select * from orders;"
    orders = orm.getData(sql)
    print("id   编号   数量  金额  折扣")
    for product in orders:
        for i in product:
            print(i, end="    ")
        print()


# 删除订单:(通过订单号删除)
def delOrder():
    num = input("请输入订单号:")
    sql = "delete from orders where num = " + num
    r = orm.writeData(sql)
    if r == 0:
        print("删除失败")
    else:
        print("订单", num, "删除成功!")


# 订单总量(总销量,销售额)
def accrdOrder():
    sql = "select * from orders;"
    data = orm.getData(sql)
    totalCount = 0
    totalAmount = 0
    for order in data:
        totalCount += order[2]
        totalAmount += order[3]
    print("总销量", totalCount, "件!,销售额", totalAmount, "元!")


# 商品结算
def settle():
    # 输入商品编号和数量
    # 计算金额
    # 重复添加多个商品
    # 计算订单总金额、数量#在订单表中添加订单
    orderCount = 0
    orderAmount = 0
    while 1 == 1:
        data = getProduct()
        num = float(input("请输入商品数量:"))
        if data != None:
            print(data)
            print(data[1])
            print(data[2])
            print(data[3])

        #     amount = price*num*discount
        #     orderCount +=num
        #     orderAmount +=amount
        #     print("当前添加了",num,"件!,金额",amount,"元")
        # r = input("继续添加输入1,结算输入2")
        # if 1==1:
        #     continue
        else:
            print("---------已结算!----------")
            break
    print("您购买的总数量", orderCount, "件!总金额元", orderAmount, "元!")
