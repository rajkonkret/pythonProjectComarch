tuple1 = "Tomek", "Michał", "Asia", "Daniel", "Anna"  # tupla jest niemodyfikowalna
tuple2 = "Radek",
tuple3 = 43, 55, 22.43, 11, 200

print(tuple1)
print(type(tuple1))
print(tuple2)  # ctrl + shift + strzałeczki
print(tuple3)  # ctrl + shift + strzałeczki
print(tuple1.count("Tomek"))
print(tuple3.count(55))
print(tuple1.index("Asia"))
asia = tuple1[2]
print(asia)

*imie1, imie2, imie3 = tuple1

print(imie1)
print(imie2)
print(imie3)
print(type(imie1))
print(type(imie2))
print(type(imie3))

lista = list(tuple1)
print(lista)
