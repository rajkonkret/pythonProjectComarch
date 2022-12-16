from datetime import date, timedelta

#
# today = date.today()
# print(today)
# print(today.year)
# print(today.timetuple())
# tomorrow = today + timedelta(days=1)
# print(tomorrow)
# products = [
#     {'sku': '1', 'exp_date': today, 'price': 100.0},
#     {'sku': '2', 'exp_date': tomorrow, 'price': 50},
#     {'sku': '3', 'exp_date': today, 'price': 20}
# ]
#
# for product in products:
#     if product['exp_date'] != today:
#         continue
#     product['price'] *= 0.8  # p = p * 0.8
#     print(
#         'Price for sku=', product['sku'],
#         'is now', product['price']
#     )

print("Podaj liczbe ocen")
lizba_ocen = int(input())
suma = 0
i = 1

while i <= lizba_ocen:
    print("Podaj ocene" + str(i) + ":")
    ocena = float(input())
    if ocena < 1.0 or ocena > 6:  # <1 >6
        continue
    suma += ocena
    i += 1

print(f"Suma ocen {suma}")
print(f"Średnia ocen {suma / lizba_ocen}")
