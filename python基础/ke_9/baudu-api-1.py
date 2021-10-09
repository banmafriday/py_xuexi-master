# baudu-api 人工智能接口


from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '24875006'
API_KEY = 'MdCiQ6UMGnKxFMMFhqOIuGSY'
SECRET_KEY = 'LaG43Fw17NuxS6sGRuaMG0Y2G1lHmQsw'

# ocr客户端对象

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
with open(r"D:\t2.jpg", "rb") as f:
    img = f.read()

# 识别文字
data = client.basicGeneral(img)
print(data)
for d in data["words_result"]:
    print(d["words"])
