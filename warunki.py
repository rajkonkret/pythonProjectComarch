# # czy_znasz_Python = False
# #
# # if czy_znasz_Python:
# #     print("Brawo")
# # else:
# #     print("Musisz sie uczyć")
# #
# # print("Jestem poza warunkiem")
# #
# # podatek = 0.0
# #
# # zarobki = int(input("Podaj swój dochód: "))
# # if zarobki < 10000:
# #     podatek = 0.0
# # elif zarobki < 30000:
# #     podatek = 0.2
# # elif zarobki < 100000:
# #     podatek = 0.35
# # else:
# #     podatek = 0.4
# #
# # print(f"Zapłacisz {zarobki * podatek} zł")
# # # pomiedzy 30 a 100 podatek 0.35
#
#
# suma_zam = 247
# if suma_zam > 100:
#     rabat = 25
# else:
#     rabat = 0
#
# print("suma zam:", suma_zam, "rabat:", rabat)
# rabat = 25 if suma_zam > 100 else 0
# print("suma zam:", suma_zam, "rabat:", rabat)
#
# lista_bledow = []
# alert_system = 'email'
# error = 'inny'
# error_message = "Stało sie cos strasznego"
# # = wpisz do zmiennej
# # == porównanie
# if alert_system == 'console':
#     print(error_message)
# elif alert_system == 'email':
#     if error == 'critical':
#         lista_bledow.append('critical')
#     elif error == 'medium':
#         lista_bledow.append('medium')
#     else:
#         lista_bledow.append("NIEZNANY")
#
# print(lista_bledow)

print("""
    Kalkulator
    """)
a = int(input("Podj liczbe 1: "))
b = int(input("Podj liczbe 2: "))
odp = input("1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie")

if odp == "1":
    # print("Wynik dodawania", a + b)
    print(f"Wynik dodawania {a} + {b} = {a + b}")
elif odp == "2":
    # print("a - b = wynik", a - b)
    print(f"a - b = wynik {a} - {b} = {a - b}")
elif odp == "3":
    print(f"a * b = wynik {a} * {b} = {a * b}")
elif odp == "4":
    if b != 0:
        print(f"a / b = wynik {a} / {b} = {a / b}")
    else:
        print("Nie dzielimy przez zero")
else:
    print("Nie znam takiego działania")
"""
Tak przerobic nasz kalkulator by wynik wypisywał wg wzoru:
a - b = wynik

5 - 6 = -1
f
"""
