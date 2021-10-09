# tushare股票价格自动监控
import tushare
import time

while 1 == 1:
    buypoint = 12
    salepoint = 5.6

    daa = tushare.get_realtime_quotes("601398")
    name = daa.loc[0][0]  # 名称
    pre_close = float(daa.loc[0][2])  # 昨收
    price = float(daa.loc[0][3])  # 现价
    chang = round((price - pre_close) / pre_close, 4)  # 今日涨幅  #(当前价格-昨收*今日涨幅)
    msg = "股票名称:," + name + ",当前价格:," + str(price) + ",元,涨幅%:" + str(chang * 100) + "%"

    print(msg)

    if price <= buypoint:
        print("价格达到买点!如果空仓请买进!")
    elif price >= salepoint:
        print("价格达到卖点点!如果持仓请卖出!")
    else:
        print("不要做任何操作")
    time.sleep(5)