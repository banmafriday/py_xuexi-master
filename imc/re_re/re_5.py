# coding:utf-8
# 贪婪非贪婪
import re

# 贪婪
a = "python 111java php"
r = re.findall("[a-z]{1,2}",a)
print(r)

#非贪婪 加?
a = "python 111java php"
r = re.findall("[a-z]{3,6}?",a)
print(r)