# import random
#
# lista = []
# for i in range(10):  # 0...9
#     if i % 2 == 0:
#         # print(i)
#         lista.append(i)
#
# # print(lista)
# #
# # lista2 = list(range(1, 50))
# #
# # for i in range(6):
# #     wyn = random.choice(lista2)
# #     print(wyn)
# #     lista2.remove(wyn)
#
# # link https://drive.proton.me/urls/Q41YAVA5X8#qeXAfYa6mGhr
#
# print(lista)
# for cyfra in lista:
#     if cyfra == 2:
#         cyfra += 1  # cyfra = cyfra + 1, +=, *=
#     print(cyfra)
#
# lista3 = [j for j in range(10) if j % 2 == 0]
# print(lista3)
#
# imiona = ["Radek", "Zenek", "Marta"]
# for p in imiona:
#     print(p)
#     print(imiona)
#
# for p in range(len(imiona)):  # range(3)
#     print(p, imiona[p])
#
# for pozycja, wartosc in enumerate(imiona):
#     print(pozycja, wartosc)
#
# imie = "Radek"
# for p, w in enumerate(imie):  # enumerate() => p = index, w = imie[p]
#     print(p, w)
#
# ludzie = ["Radek", "Janek", "Asia", "Michał"]
# wiek = [47, 67, 32, 34]
# jezyk = ["java", "python"]
#
# for pozycja, osoba in enumerate(ludzie, start=1):
#     print(pozycja, osoba)
#
# for pozycja, osoba in enumerate(ludzie):
#     print(pozycja, osoba, wiek[pozycja])
#
# for osoba, wiek, jezyk in zip(ludzie, wiek, jezyk):
#     print(osoba, wiek, jezyk)
#
# slownik = {"imie": "Radek", "nazwisko": "Kowalski"}
# for k in slownik:
#     print(k)
#
# for v in slownik.values():
#     print(v)
# for k in slownik.keys():
#     print(k)
#
# for k, v in slownik.items():
#     print(k, "=>", v)
#
# slownik2 = {"test": 1, "test2": 2}  # klucz, wartosc
# for k, v in slownik2.items():
#     print(k, "=>", v)
# # 13: 50
imie = "Radek"
for i in range(-1, -len(imie)-1, -1):  # range(-1,-5,-1)
    j = i + 1
    if j == 0:
        print(imie[i::])  # [-1:]
    else:
        print(imie[i:j])

for i in range(1, 10, 2):  # (start, koniec,krok)
    print(i)
