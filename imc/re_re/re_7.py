# coding:utf-8
#边界匹配
import re

qq = "1000001"

# 前获取5位数

r = re.findall("\d{4,5}",qq)
print(r)

# ^从第一位开始匹配,&从最后一位开始匹配
r = re.findall("001&",qq)
print(r)