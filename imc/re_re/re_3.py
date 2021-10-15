# coding:utf-8
# 字符集
import re

s = "abc,acc,adc,aec,afc,ahc"
r = re.findall('a[bcd]c', s)  # 中间包含字符
print(r)

s = "abc,acc,adc,aec,afc,ahc"
r = re.findall('a[^bcd]c', s)  # 中间不包含字符
print(r)

s = "abc,acc,adc,aec,afc,ahc"
r = re.findall('a[b-f]c', s)  # 获取b到f中间的值
print(r)
