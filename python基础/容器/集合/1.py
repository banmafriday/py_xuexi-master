# 集合set
# 无序，元素不重复
aset = {12,3432,432,432,"4324",432432,}
print(aset)

# 去除重复值
lista = [1,2,3,4,5,5,5,5,5,5,5,5,5,5]
seta = set(lista)   # 将其他序列转换成set
print(seta)

zh = list(seta)  # 将其他序列转换成list
print(type(zh))



# 集合运算
setaa = {1,2,3,4,5,6}
setbb = {7,8,9,4,5,6}

print(setaa&setbb)   #获取交集,获取相同的值
print(setaa|setbb)   #获取并集，获取不相同的值
print(setaa-setbb)   #获取差集，获取setbb没有的值
print(setbb-setaa)   #获取差集，获取setaa没有的值