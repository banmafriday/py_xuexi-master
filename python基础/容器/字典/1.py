# 字典
# 键:值
# 特性:无序:键值对形式:键不可以重复,一般使用字符串作为键
adicta = {"name":"张三","age":18,"hobby":"playBall"}


# 使用键获取值
print(adicta["name"])
print(adicta["age"])
print(adicta["hobby"])

# 修改字典的值
adicta = {"name":"张三","age":18,"hobby":"playBall"}
adicta["hobby"]="看书"
print(adicta)

# 增加字典数据
adicta["banma"] = "男"
print(adicta)

#删除字典数据
adicta.pop("age")
print(adicta)

# 判断一个键是否存在
print("banma"in adicta)