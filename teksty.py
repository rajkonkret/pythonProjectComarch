a = 14
b = 3
print(f"Wynik porównania {a} > {b}", a > b)
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)
print(f"Wynik porównania {a} != {b}", a != b)  # różne

tekst = "Witaj świecie"
tekst2 = tekst.upper()

print(tekst2)
print(tekst)
print(tekst.lower())
print(tekst.removeprefix("Witaj "))
print(tekst.removesuffix("świecie"))

# utf-8
encoded_s = tekst.encode('utf-8')
print(type(encoded_s))
print(encoded_s)
print(encoded_s.decode('utf-8'))
print(type(encoded_s.decode('utf-8')))
tekst_bajtowy = b"Tutaj jest tekst bajtowy"
print(tekst_bajtowy)

print(len(tekst))  # długosc tekstu
print(tekst.count("i"))
print(tekst.count("i", 0, 4))

imie = "Radek"
starszy = "Witaj %s"
print(starszy % imie)
tekst_format = f'Mam na imie {imie}'
print(tekst_format)

imie = input("Podaj imie")
if imie == "Radek":
    print(f"Czesc {imie}")
else:
    print("Nie zna Cię")
