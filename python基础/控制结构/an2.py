
dong_name = "东三省"
dong_id = "1"
jia_fii = 12


xx_name = "新疆、西藏"
xx_id = "2"
jia_xx = 20


guo_name = "国外"
guo_id = 3


dian = input("请输入地点：")
zhong = float(input("请输入重量："))

zhong_result = 0
ding_result = ""

if dian == dong_id:
    ja = jia_fii
    re1 = zhong * ja

    if zhong <= 3:
        print(re1)

