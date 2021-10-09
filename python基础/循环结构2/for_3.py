# 最大值,最小值
scores = [234, 4324, 32, 4, 32, 4, 32, 4, 3111111111111111112, 4, 432, 4, 32, 4]
to = scores[0]
for co in scores:
    if co < to:
        to = co
print(to)
