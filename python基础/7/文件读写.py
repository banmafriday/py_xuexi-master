# 读文件
f = r"C:\\Users\\banma\\Desktop\\t.txt"
file = open(f,"r",encoding="utf-8")
data = file.read()
file.close()
print(data)