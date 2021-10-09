# global将函数内部的a设置为全局变量
a = "北京"


def fun():

    global a  # 将函数内部的a设置为全局变量
    a = "广东"


fun()
print(a)
print(a)