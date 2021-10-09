# 字符串拼接
a1 = "张三"
a2 = "椰林"
a3 = "斑马"
d = a1 + a2 + "rfewrewrew"
print(a1 + a2 + a3)
print(d)

# format函数拼接
s1 = "hello!{}".format("张三")  # 单个
s1 = "hello!{}{}".format("张三", "斑马")  # 多个
S2 = "hello{a}{b}{c}".format(a="xx", b="bb", c="oo")
print(S2)
print(s1)

# 转义字符 换行
sc = "这是第一行！\n这是第二行"
print(sc)

# 制表符 \t  4个空格
sc1 = "离我\t 远点"
sc1 = "离我\t\t \t \t \t \t \t \t \t \t  远点"

print(sc1)

# 取消转义
scc11 = r"D:\auth\daima"

scc121 = r"D:\\auth\\daima"  # 双重转义等于不转义
print(scc11)
print(scc121)
