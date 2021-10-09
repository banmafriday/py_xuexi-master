# coding:utf-8

# 获取异常,当异常发生时,获取异常信息并作相应处理,避免程序崩溃
#只能捕获运行时异常,如果代码本身不能正常运行比较语法错误,缩进错误,不能捕获
lista = [10, 12, 0, 43, 46]
for i in lista:
    try:
        r = 10 / i
        print(r)
    except Exception as e:  # Exception错误的类型    e保存具体错误内容
        print("出现错误", e)
