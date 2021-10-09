import requests

# 抓包获取音乐链接
url = "https://m801.music.126.net/20210922214719/686ea8756b009f7a71505eda53184fa" \
      "e/jdyyaac/515a/535c/005a/f0b69b1e99d620cf96ac70c22ee65eba.m4a"

# content获取二进制数据
# txt获取二进制数据
data = requests.get(url).content

# 写入本地
with open(r"F:\py\音乐1.m4a", "wb") as  f:
    f.write(data)

