# coding:utf-8
# 概括字符集
import re

# \w匹配单词字符    \匹配非单词(特殊符号)  \s空白字符
a = 'Pyt0hon0|Jav\t9a*&|5e\nwq555_'
r = re.findall('\s', a)  # 获取所有值
print(r)
