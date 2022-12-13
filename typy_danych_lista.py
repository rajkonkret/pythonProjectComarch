lista = []

lista.append("Radek")
lista.append("Magda")
lista.append("Renata")
print(lista)
lista.insert(1, "Darek")

print(lista)

lista[1] = "Krzysiek"
print(lista)
lista.remove("Renata")
print(lista)
lista.append("a")
lista.reverse()
print(lista)
lista2 = lista.copy()
print(lista2)

liczby = [54, 999, 34, 22, 12.54, 876]
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby2 = liczby.copy()
print(liczby2)
liczby.clear()
print(liczby)
print(liczby2)
liczby2[0] = 6666
print(liczby2)
print(liczby2[0:3])
print(liczby2[:3])
print(liczby2[2:])
print(liczby2[:-1])
print(liczby2)
print(len(liczby2))  # długosc kolekcji / ilosc elementow)
liczby2.remove(54)
print(liczby2)
print(len(liczby2))

krotka = tuple(liczby2)
print(krotka)
