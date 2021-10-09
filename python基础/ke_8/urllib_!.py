# 内置模块urllib(爬虫模块)
# 爬虫:爬取互联网数据的程序
from urllib import request

url = "http://www.baidu.com"
data = request.urlopen(url).read()  #发送请求,读取数据
print(data.decode())            #decode解码,将二进制转换成字符

with open(r"03.html","wb") as f:
    f.write(data)
