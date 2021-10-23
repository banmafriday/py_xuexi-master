# coding:utf-8
# 闭包
origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        nwe_pos = pos + step
        pos = nwe_pos
        return nwe_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))