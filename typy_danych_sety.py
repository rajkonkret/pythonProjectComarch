lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)

print(lista)
print(zbior)

zbior.add(18)
zbior.add(18)
zbior.add(32)

print(zbior)
print(zbior.pop())  # 32
print(zbior.pop())  # 33
print(zbior.pop())  # 66

lista2 = list(zbior)
print(lista2)
print(zbior)

print(type(zbior))

zbior2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior2)
print(zbior | zbior2)  # potoczna suma or
print(zbior & zbior2)  # potoczna czesc wspolna and
print(zbior - zbior2)
print(zbior2 - zbior)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
