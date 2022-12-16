# hackerrank
a = 10


def dodaj():
    global a
    a = 4
    b = 10
    print("Wynik ", a + b)


def dodaj2(a):
    a = 4
    b = 2
    return a + b


print("Wartosc a z gory", a)
dodaj()
print("Wartosc a z gory", a)
print(dodaj2(a))
print("Wartosc a z gory", a)
