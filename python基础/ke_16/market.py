# coding:utf-8
# 编写业务方法
import orm


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
    sql = "select * from Products where num = " + num
    data = orm.getData(sql)
    print("商品名称:",data[0],"单价:",,"折扣:"",,")


# 添加商品
def addProduct():
    pass


# 根据编号删除商品
def delProduct():
    pass


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
    pass
