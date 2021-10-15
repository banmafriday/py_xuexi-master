# coding:utf-8
import re

a = 'Python|Java'
ab = re.findall('Python', a)  # 查找全部
if len(ab) != 0:
    print(ab)
