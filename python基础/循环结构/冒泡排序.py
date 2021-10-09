lista = [5, 4, 3, 2, 1]
for x in range(1, len(lista) - 1 + 1):

    for y in range(0, len(lista) - x - 1 + 1):

        # 两个数交换值
        if lista[y] < lista[y + 1]:
            c = lista[y]
            lista[y] = lista[y + 1]
            lista[y + 1] = c
print(lista)

a =10
b=20

c = a
a = b
b=c
print(a,b)