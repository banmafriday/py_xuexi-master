# coding:utf-8
# 列表推到式
# set集合也可以被推导
# 求平方 列表
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a]
print(b)


# 求立方 set集合
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {i ** 3 for i in a}
print(b)

# 筛选单个元素   元组
a = (1, 2, 3, 4, 5, 6, 7, 8)
b = (i ** 2 for i in a if i==5)   # 筛选5
print(b)

# 字典推导
students={
    '喜小乐':18,
    '石敢当':20,
    '小王':15
}

b = [key for key,value in students.items()]
print(b)

# 元组推导
students={
    '喜小乐':18,
    '石敢当':20,
    '小王':15
}

b = (key for key,value in students.items())
for i in b:
    print(i)