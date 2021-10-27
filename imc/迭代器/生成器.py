# coding:utf-8
# 生成器

def gen(max):
    n = 0
    while n<=max:
        n+=1
        yield n


g = gen(100000)
print(next(g))  # 只调用一次

for i in g:    # 调用100000 次
    print(i)