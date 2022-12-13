licznik = 0

while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat...")
    if licznik == 10:
        break

licznik = 0
while licznik < 10:
    print("Komunikat...")
    licznik += 1

lista = []
#
# while True:
#     wejscie = input("Wprowadz liczbe")
#     if wejscie.lower() == "s":
#         break
#     lista.append(wejscie)

lista = [4, 6, 8, 10]
people = ["Radek", "Kuba", "Agata", "Anna"]
pos = 0

while pos < len(people):
    person = people[pos]
    liczba = lista[pos]
    print(person, liczba)
    pos += 1

liczby = []
# while True:
#     print("Wprowadz liczbe")
#     liczba = input(":")
#     liczby.append(liczba)
#     if liczba == "stop":
#         for i in liczby:
#             print(i * 2)
#         break
print(liczby)
imie = "Radek"

n = len(imie)
if n > 3:
    print(imie, n)

if (n := len(imie)) > 3:  # := n = len(imie), n > 3
    print(imie, n)

# Napisac kalkulato, ktory wyswietla menu z działaniami i z opcja koniec
# koniec ma przerywac działanie kalkulatora

# while True:
#     a = int(input("Podaj liczbe 1"))
#     b = int(input("Podaj liczbe 2"))
#     print("""
#         Kalkulator
#         1. Dodawanie
#         2. Odejmowanie
#         3. Mnozenie
#         4. Dzielenie
#         5. Koniec
#         """)
#     wybor = input("Wprowadz numer (1-5)")
#     if wybor == "1":
#         print(f"Dodajemy: {a + b}")
#     elif wybor == "2":
#         print("Odejmujemy", a - b)
#     elif wybor == "3":
#         print("Mnożymy", a * b)
#     elif wybor == "4":
#         print("Dzielimy", a / b)
#     else:
#         print("Dziekujemy")
#         break

slownik = {1: "Tomek", 2: "Kuba"}
print(slownik)
print({value: key for key, value in slownik.items()})

slownik2 = {}
for key, value in slownik.items():
    slownik2[value] = key

print(slownik2)
slownik3 = {"imie": "Radek", "imie": "Karol"}
print(slownik3)
