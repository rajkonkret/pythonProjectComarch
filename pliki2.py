# fh = open('dane.txt', 'a')  # a - append - dodawanie na koncu pliku
# fh.write("Test nr 11\n")
# fh.write("Test nr 12\n")
# fh.write("Test nr 13\n")
# fh.close()
#
# # nie ma trybu w jaki otwieramy czyli domyslnie 'r'
# with open('dane.txt') as fh:
#     for line in fh:
#         print(line.strip())

lista = [1, 2, 3, 4]
print(type(lista))
tmp = str(lista)
print(type(tmp))

with open('dane.txt', 'w') as fh:
    fh.write(str(lista))

lista2 = []

with open('dane.txt', 'r') as fh:
    for line in fh:
        lista2.append(line.strip())
print(lista2)
print(type(lista2))
print(len(lista2))
lista_x = ['[a,c]']
print(len(lista_x))

for i in lista2:
    print(i)

print(lista2[0])
print(type(lista2[0]))
print(lista2[0][0])
print(lista2[0][1])
print(lista2[0][2])

