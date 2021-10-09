# 返回值
# def fun1(lsta):
#     r = sum(lsta) / len(lsta)
#     return r
#
#
# result = fun1([2, 324, 32, 4, 32])  # 接受返回值
#
# print(result)


# 返回多个值
#
# def fun2():
#     print("fun2被执行了")
#     a = 1
#     b = 2
#     c = 3
#     return a, b, c
#
#
# r1, r2, r3 = fun2()
# print(r1, r2, r3)

# 榨汁机
def juicer(f1):
    print("榨汁机开始工作")
    juice = f1 + "汁"
    return juice


j = juicer("苹果")
print(j)
