# coding:utf-8

a = 1

list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x

#
# for i in list_x:
#     print(square(i))
r = map(square,list_x)
print(list(r))