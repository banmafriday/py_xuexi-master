# coding:utf-8
# 过滤

list_x = [1, 0, 0, 1, 1, 6, 1, 6]
r = filter(lambda x: True if x == 6  else False, list_x)  # 保留6,去除0和1
print(list(r))

# 第二种写法

list_y = [1, 0, 0, 1, 1, 1, 1, 1, 6, 5]
r = filter(lambda x: x, list_y)  # 保留1,去除0和6
print(list(r))
