# 读二进制文件


file = open(r"F:\1.png", "rb")
data = file.read()
file.close()
print(data)

# 写文件
file2 = open(r"F:\bbb\132432_1.png", "wb")
file2.write(data)
file2.close()

print("斑马")