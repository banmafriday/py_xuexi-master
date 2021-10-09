#文件复制
with open(r"F:\aaa\1.png","rb")as file1,open(r"F:\bbb\1_!.png","wb")as file2:
    data = file1.read()
    file2.write(data)
