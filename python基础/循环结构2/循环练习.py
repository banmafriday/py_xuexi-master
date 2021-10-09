# to = 0
# for i in range(1,6):
#     nu = int(input("请输入5个数"))
#     to = to+nu
# print(to/5)

p = 0.08
m = 8848000
to = 0
while p < m:
    p =p*2
    to = to+1
    print(to,round(p))