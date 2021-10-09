# 列表 list
# 特性 ：有序,元素可以重复，可以存放多种数据类型

# 通过索引（下标）获取值
list1 = ["张三", "椰林", 666]

print(list1[1])
print(list1[-2])

# 切片 截取列表的一部分
list1 = ["张三", "椰林", 666]
print(list1[1:2])

# 步长
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list2[0:8:3])

print(list2[8:])  # 获取某个索引最后的值

print(list2[:8])  # 获取某个索引前面的值

# 给列表增加数据
list1d = ["张三", "椰林"]
list1d.append("大宝")  # 在尾部添加
list1d.insert(2, "乔峰")  # 在指定位置添加元素
print(list1d)

# 给列表删除数据
list1dd = ["张三", "椰林"]
list1dd.remove("张三")  # 删除一个具体值
list1dd.pop(0) #删除指定位置的值
print(list1dd)

# 给列表重新赋值
list1d1dd = ["张三", "椰林"]
list1d1dd[0]="张三丰"
print(list1d1dd)