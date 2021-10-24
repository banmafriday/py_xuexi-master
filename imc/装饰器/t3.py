# coding:utf-8
# 装饰器--不带参数
import time
# def decorator(funt):
#     def wrapper():
#         print(time.time())
#         funt()
#     return wrapper
#
# @decorator
# def f1():
#     print("This is a function")

# 装饰器--带1个参数
import time


def decorator(func):
    def wrapper(*args,**kw):  # args 可变参数 可传任意的参数   # kw可以任意命名
        print(time.time())
        func(*args,**kw)  # args 可变参数 可传任意的参数

    return wrapper


@decorator
def f1(func_name):
    print("This is a function" + func_name)


@decorator
def f2(func_name1, func_name2):
    print("This is a function" + func_name1 + func_name2)


@decorator
def f3(func_name1, func_name2,**kw):
    print("This is a function" + func_name1 + func_name2)
    print(kw)


# f1("tst")
#
# f2("test1", "test2")

f3('test ','test2',a=1,b=2 ,c='123')