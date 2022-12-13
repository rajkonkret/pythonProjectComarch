slownik = {}

print(slownik)
slownik["imie"] = "radek"
slownik["imie"] = "Zenek"
print(slownik["imie"])
print(slownik)
slownik["wiek"] = 39
print(slownik)

print(slownik.items())
print(slownik.values())
print(slownik.keys())

lista = [44, 55, 66, 77, 88, 33, 22, 11, 55, 33, 11]
slownik['liczby'] = lista
print(slownik)

print(slownik['liczby'])
print(slownik['liczby'][0])

lista2 = [44, 55, 66, 11]
nowa_lista = lista2 + lista
print(nowa_lista)

slownik2 = {'imie': ["Radek", "Krzysztof"]}
print(slownik2)

slownik3 = {'imie': 'name', "kot": 'cat'}

print(slownik3['kot'])

# print("Mamy tyle w słowniku", slownik3.keys())
# key = input("Podaj wyraz do przetłumaczenia")
# key2 = key.replace(" ", "")
# print(key2)
# print(slownik3[key2])

slownik3.update({"pies": "dog"})
print(slownik3)

a = "34"
print(a)
print(type(a))
a = 34
print(a)
print(type(a))

li1 = int(input("podaj liczbe 1"))  # input zwraca stringa
li2 = int(input("podaj liczbe 2"))  # rzutujemy na int

print(li1 + li2)
