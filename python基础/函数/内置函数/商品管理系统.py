# 数据准备
user1 = {"用户名": "aaa", "密码": "123", "姓名": "张三"}
user2 = {"用户名": "bbb", "密码": "123", "姓名": "李四"}
user3 = {"用户名": "ccc", "密码": "123", "姓名": "王五"}
usersList = [user1, user2, user3]  # 用户列表

p1 = {"编号": "1001", "名称": "苹果", "价格": "5", "折扣": "1"}
p2 = {"编号": "1002", "名称": "香蕉", "价格": "3", "折扣": "1"}
p3 = {"编号": "1003", "名称": "牛奶", "价格": "2", "折扣": "1"}
p4 = {"编号": "1004", "名称": "白菜", "价格": "1", "折扣": "1"}
p5 = {"编号": "1005", "名称": "西瓜", "价格": "5", "折扣": "1"}
productsList = [p1, p2, p3, p4, p5]


# 登录
def login():
    msg = "失败"
    while 1 == 1:
        uname = input("请输入用户名:")
        print(uname)
        upwd = input("请输入密码:")
        print(upwd)
        for user in usersList:
            if uname == user["用户名"] and upwd == user["密码"]:
                print("------------验证成功!欢迎你", user["姓名"], "-----------------")
                msg = "成功"
                break
        if msg == "失败":
            print("用户名密码输入错误,请重新输入")
            continue
        else:
            break
    return msg  # 返回登录结果


# 1、显示商品列表
def showProcucts():
    print("------编号------名称-----价格-------折扣------")
    for product in productsList:
        print(product["编号"] + "---" + product["名称"] + "---" + str(product["价格"]) + "---" + str(product["折扣"]))
    print("-------------------------------")


# 2、增加商品信息
def addProcucts():
    # 生成新的编号
    lista = []  # 存放所有的编号
    for produc in productsList:
        lista.append(int(produc["编号"]))
    nweNum = str(max(lista) + 1)
    name = input("请输入商品名称：")
    price = float(input("请输入商品折扣："))
    nweProduct = {"编号": nweNum, "名称": name, "价格": price, "折扣": 1}
    productsList.append(nweProduct)
    print("-------商品", name, "添加成功！-------------")
    showProcucts()


# 3、 删除商品(通过编号删除)
def delProcucts():
    while 1 == 1:
        msg = 0  # 记录商品是否存在
        num = input("请输入要删除的商品编号")
        for product in productsList:
            if num == product["编号"]:
                print("正在删除", product["名称"], "商品.........")
                productsList.remove(product)  # 删除商品
                print("删除成功!")
                msg = 1
                break
        if msg == 0:
            print("商品编号不存在")
            choice = int(input("取消请按1,重新输入请按2"))
            if choice == 1:
                break
            else:
                continue

        else:
            showProcucts()
            break


# 4、设置商品折扣
def setDiscout():
    while 1 == 1:
        msg = 0  # 记录商品是否存在
        num = input("请输入要设置折扣的商品编号")
        for product in productsList:
            if num == product["编号"]:
                nweDiscou = float(input("请输入新的折扣(0.1-1)"))
                product["折扣"] = nweDiscou  # 设置折扣
                print("商品", product["名称"], "折扣已设置成功,", nweDiscou * 10, "折!")
                msg = 1
                break
        if msg == 0:
            print("商品编号不存在")
            choice = int(input("取消请按1,重新输入请按2"))
            if choice == 1:
                break
            else:
                continue
        else:
            break


#  5、修改商品价格信息
def setPrice():
    while 1 == 1:
        msg = 0  # 记录商品是否存在
        num = input("请输入要设置价格的商品编号")
        for product in productsList:
            if num == product["编号"]:
                nwePrice = float(input("请输入新的价格(0.1-1)"))
                product["价格"] = nwePrice  # 设置价格
                print("商品", product["名称"], "价格已设置成功,", nwePrice, "元!")
                msg = 1
                break
        if msg == 0:
            print("商品编号不存在")
            choice = int(input("取消请按1,重新输入请按2"))
            if choice == 1:
                break
            else:
                continue
        else:
            showProcucts()
            break


# 根据价格排序显示商品列表
def sort():
    choice = int(input("请选择升序或者降序(1升序,2降序)"))
    plist = []  # 存放所有价格信息

    for product in productsList:
        plist.append(product["价格"])
    plist = list(set(plist))  # 去掉重复的价格
    print("------编号------名称-----价格-------折扣------")
    if choice == 1:
        nweList = sorted(plist)
        for price in nweList:
            for product in productsList:
                if price == product["价格"]:
                    print(
                        product["编号"] + "---" + product["名称"] + "---" + str(product["价格"]) + "---" + str(product["折扣"]))

    else:
        nweList = sorted(plist, reverse=True)
        for price in nweList:
            for product in productsList:
                if price == product["价格"]:
                    print(
                        product["编号"] + "---" + product["名称"] + "---" + str(product["价格"]) + "---" + str(product["折扣"]))


# 显示主菜单，调用已经写好的业务函数
while 0 == 0:
    result = login()
    if result == "成功":
        while 2 == 2:
            print("-------------主菜单-----------")
            print("-------------1.显示商品列表----------------")
            print("--------------2.增加商品信息---------------")
            print("--------------3.删除商品---------------")
            print("--------------4.设置商品折扣---------------")
            print("--------------5.修改商品信息---------------")
            print("--------------6.按照价格排序---------------")
            print("--------------7.退出---------------")

            choice = int(input("请选择业务编号(输入1--6):"))
            if choice == 1:
                showProcucts()
            elif choice == 2:
                addProcucts()
            elif choice == 3:
                delProcucts()
            elif choice == 4:
                setDiscout()
            elif choice == 5:
                setPrice()
            elif choice == 6:
                sort()
            elif choice == 7:
                print("---*-正在退出--*-")
                break
            else:
                print("没有此功能,请重新选择")
                continue

