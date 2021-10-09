# 元组 tuple
# 特性:有序的;元素可重复:可存放多种数据类型
# 不支持元素的修改
# 元组用在对安全性有一定需求的数据上
# tuple1 = ("张三","李四","王五","需要")
# print(tuple1[1])
# print(tuple1[-1])
# print(tuple1[1:3])

# 多维容器
alista = [113,2432,43,535,16,1]
blistb = [213,2432,43,"你好",535,56,2]
clista = [313,2432,43,535,56,3]
xlist=[alista,blistb,clista,[21,33,22,33,55,66]]
print(xlist[1][3])

cxlist=[alista,blistb,clista,("斑马"),[21,33,22,33,("张三"),55,66]]
print(cxlist[3])
