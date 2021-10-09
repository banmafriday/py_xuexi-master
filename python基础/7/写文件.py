# 创建一个txt文件
#如何文件不存在，则创建
# 如果文件存在，则覆盖

# s = "!!你好上海!!!!!!!!!!!"
#
# file = open(r"F:\rttt.txt", "w")
#
# file.write(s)
# file.close()

#追加写入

s = "巴麻美"

file = open(r"F:\rttt.txt", "a")

file.write(s)
file.close()