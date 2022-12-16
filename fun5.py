# def liczby(c, *cyfry):
#     suma = 0  # mozna zrobic suma=c gdy chcemy by tez dodawał to co przyjdzie w c
#     count = len(cyfry)
#     print(c)
#     print(cyfry)
#     print(type(cyfry))
#     for i in cyfry:
#         suma += i
#     print(f"suma {suma}", f"średnia {suma / count}")
#
#
# # liczby(5, 1)
# # liczby(5, 4, 43, 7, 67, 8, 9, 0, 0, 14, 56 )
# # liczby(3, 4)
#
#
# def connect(**opcje):  # ** - zamiana na słownik
#     connect_param = {
#         'host': '127.0.0.7',
#         'port': '8080',
#         'user': 'admin',
#         'pass': '123456'
#     }
#     connect_param['pwd'] = opcje
#     print(connect_param)
#     print(opcje)
#
#
# connect(user='/home', root='/')
#
#
# def dodaj(a, b):
#     print(a + b)
#
#
# def sumuj(*cyfry):
#     suma = 0
#     for i in cyfry:
#         suma += i  # suma = suma + i
#     print(suma)
#
#
# dodaj(1, 2)
# sumuj(1, 2, 3, 4, 5, 6)
# sumuj(1, 2, 3, 4, 5, 6, 7, 8, 23, 34)
#
#
# def ujmuj(*cyfry):
#     sum = 0
#     for i in cyfry:
#         sum -= i
#     print(sum)
#
#
# ujmuj(1, 2, 3)
#
#
# def wypisz(a, b, c):
#     print(f"a={a} b={b} c={c}")
#
#
# wypisz(1, 2, 3)
# wypisz(c=1, a=2, b=3)
#
#
# def wypisz_1(a, b, /, c):
#     print(f"a={a} b={b} c={c}")
#
#
# wypisz_1(1, 2, 3)
# wypisz_1(1, 2, c=2)


def allparams(a, b, /, c=42, *args, d=256, e, **kwargs):
    print('a, b, c:', a, b, c)
    print('d, e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)


allparams(2, 6, 7, 8, 9, 10, d=12, e=10, f=11)
allparams(2, 6, 7, 8, 9, 10, d=12, e=20, f=11, g=20, h=90, i="Radek")
