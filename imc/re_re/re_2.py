# coding:utf-8
import re

a = 'Pyt0hon0|Jav9a|5ewq555'
re2 = re.findall('\d',a)     # 获取所有数字
print(re2)


re2 = re.findall('\D',a)     # 获取所有非数字
print(re2)