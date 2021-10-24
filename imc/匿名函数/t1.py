# coding:utf-8
# 匿名函数
# lambda表达式
def add(x, y):
    return x + y


print(add(1, 2))

f = lambda x, y: x + y
print(f(1, 2))

# x,y =
# 条件为真时返回的结果
x = 2
y = 1
r = x if x >y else y
print(r)