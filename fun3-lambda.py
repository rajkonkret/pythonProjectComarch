odejmij = lambda a, b: a - b
print(odejmij(5, 3))

oblicz_vat = lambda cena, vat: cena * (100 + vat) / 100
print(oblicz_vat(1000, 23))

vat1 = oblicz_vat(1000, 7)
print(vat1)

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(5))
print(wiek(15))
print(wiek(25))

lista = [1, 2, 7, 8, 10, 55]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
# x > 3 and x < 20 to jest to samo 3 < x < 20
