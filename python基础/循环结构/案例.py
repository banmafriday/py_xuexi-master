care1 = {"姓名": "张三", "卡号": "1001", "密码": "123", "余额": "10000"}
care2 = {"姓名": "李四", "卡号": "1002", "密码": "123", "余额": "20000"}
care3 = {"姓名": "王五", "卡号": "1003", "密码": "123", "余额": "30000"}
care4 = {"姓名": "赵六", "卡号": "1004", "密码": "123", "余额": "40000"}

cardList = [care1, care2, care3, care4]

msg = 0  # 记录登录状态  0失败  1成功
count = 0
while 1 == 1:
    cnum = input("请输入卡号:")

    cpwd = input("请输入密码")
    for card in cardList:
        if cnum == card["卡号"] and cpwd == card["密码"]:
            msg = 1
            count = 0  # 当验证成功错误次数清0
            print("恭喜你!", card["姓名"], "!成功")
    if msg == 0:
        count += 1
        if count == 3:
            print("密码错误超过3次,银行卡已被锁定")
            break
        else:
            print("您已经输入了多少次",count,"还有",3-count,"次机会")
            continue

    # 银行业务
    while 2 == 2:
        choice = int(input("请输入要办理的业务(1.存款,2.取款,3.退出)"))

        if choice == 1:
            money1 = float(input("请输入存款金额:"))
            for card in cardList:

                if card["卡号"] == cnum:
                    card["余额"] = card["余额"] + money1
                    print("存款成功,存入", momer1, "余额", card["余额"])
                    break

        elif choice == 2:
            money2 = float(input("请输入取款金额:"))
            for card in cardList:

                if card["卡号"] == cnum:
                    card["余额"] = card["余额"] - money2
                    print("取款成功,存入", momer2, "余额", card["余额"])

                    break
        elif choice == 3:
            print("--------已退出!-----------")
        break
    else:
        print("没有此业务,请重新选择!")
        continue
