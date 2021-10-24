# coding:utf-8
from functools import reduce
#  reduce  连续计算,连续调用lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


r = reduce(lambda x, y: x + y, list_x,10)  # 10是初始值,第一次计算时用的
st = int(r)
print(st)


