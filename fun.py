a = 5
b = 5


def dodaj():
    print("Wynik =", a + b)


def dodaj2(a, b):
    print("Wynik =", a + b)


def odejmij(a, b, c=0):
    print("Wynik =", a - b - c)


def dodaj3(a, b, c=0, d=0):
    print("Wynik =", a + b + c + d)


def mnozenie(a, b):
    wynik = a * b
    return wynik


def mnozenie2(a, b):
    return a * b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


def oblicz_vat2(cena, vat):
    return cena * (100 + vat) / 100


oblicz_vat3 = lambda cena, vat: cena * (100 + vat) / 100  # def  return

print(oblicz_vat(1000))
print(oblicz_vat2(1000, 27))

print(oblicz_vat3(1000, 23))

odejmij2 = lambda a, b: a - b

print(odejmij2(8, 9))

o = 10
p = 15
odejmij(o, p)
odejmij(a=o, b=p)
print(a)
# dodaj()
# dodaj2(3, 4)
# odejmij(2, 1)
# odejmij(2, 1, 4)
# dodaj3(1, 2)
# dodaj3(b=3, a=7)
# dodaj3(1, 2, 3, 4)
# dodaj3(1, 2, 3)
# imie = "radek"
# print(imie.upper())
# print(dodaj3(1, 2))
# print(mnozenie(2, 3))
# print(mnozenie2(2, 3))
# dodaj3(mnozenie(3, 4), 1)
