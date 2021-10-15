# coding:utf-8
# 枚举
from enum import Enum


class VIP(Enum):
    YE = '1'
    GR = '1'
    BL = '3'
    RE = '4'


# 获取枚举的值
print(VIP.YE.value)


# 获取枚举的标签()
print(VIP.YE.name)

# 遍历枚举
for i in VIP:
    print(i)

