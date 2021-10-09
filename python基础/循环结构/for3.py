# # for循环
# # 求和
# # 大宝买车时，贷款12万，分10年还清
# totalMoney = 0  # 保持累计还款金额
# for year in range(1, 11):
#     totalMoney = totalMoney + 1.2
#     print("第", year, "年到了!还款1.2!累计已", round(totalMoney, 2), "还剩", round(12 - totalMoney, 2), "万")
#
# # 1-100之间所有的数
# t = 0
# for x in range(1, 101):
#     t = t + x
#
# print(t)
#
# # 最大值 最小值
#
# scores = [32, 432, 432, 5, 43, 54, 35, 43, 5, 43, 543]
# max = [0]
#
# for i in scores:
#     max = scores + max
#
#     print(i)
#
# scores = (32, 432, 432, 5, 43, 54, 35, 43, 5, 43, 543)
# code = 0
# for i in scores:
#     code= i+code
#     print(code/len(scores))
# fo = 0
# for code in range(1, 11):
#     fo = fo + 1.2
#     print("第",code,"年还了",round(fo),"万","还剩下",round(12-fo),"万")

# 1-100之间所有的和
# t=0
# for i in range(1,101):
#     t = t+i
# print(t)
#

scores = (32, 432, 432, 5, 43, 54, 3533333333333333333333333, 43, 5, 43, 533343)
t = scores[0]
for code in scores:
    if code>t:
        t = code
print(t)