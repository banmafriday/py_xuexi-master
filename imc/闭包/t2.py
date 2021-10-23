# coding:utf-8
# 非闭包
orgin = 0


def go(step):
    global orgin
    nwe_pos = orgin + step
    orgin = nwe_pos
    return nwe_pos


print(go(2))
print(go(3))
print(go(6))
