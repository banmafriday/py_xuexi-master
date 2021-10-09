
# for year in range(1,11):
#     print("第",year,"年")
#     for month in range(1,13):
#         print("第",month,"月,还款1000")
#
#         for ri in range(1,31):
#             print("第", ri, "日,还款3.3")

# 遍历多维容器

lista = [324,32,4,324,32,4,32432,4,23]
listb = [324,3243243232,4,324324324,32,4,32,4,23]
listc = [324,32,4324324324,324,32,4,32,4,23]
listx = [lista,listb,listc]

for x in listx:
    for s in x:
        print(s)