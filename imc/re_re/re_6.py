# coding:utf-8


import re

# * 匹配0次或无限次
a = "pytho0python1pythonn2java"
r = re.findall("python*",a)
print(r)

# + 匹配一次或者无限次
a = "pytho0python1pythonn2java"
r = re.findall("python+",a)
print(r)

# ? 匹配0次或者一次
a = "pytho0python1pythonn2java"
r = re.findall("python?",a)
print(r)