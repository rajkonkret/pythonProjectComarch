def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        print("Bład, zwracam bezpieczne 0")
        return 0


def mnozenie_2(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        print("Bład typu, zwracam bezpieczne 0")
        return 0
    except ValueError:
        print("Bład wartości, zwracam bezpieczne 0")
        return 0


def dzielenie(a, b):
    try:
        return int(a) / int(b)
    except TypeError:
        print("Bład typu, zwracam bezpieczne 0")
        return 0
    except ValueError:
        print("Bład wartości, zwracam bezpieczne 0")
        return 0
    except ZeroDivisionError:
        print("Nie dziel przez zero")
        return 0
11:35

print(mnozenie(3, 4))
print(mnozenie("3", "4"))
print(mnozenie("a", "b"))
print("Program działa dalej")
print(mnozenie_2("a", "b"))  # błąd wartości
print(mnozenie_2(2.8, 5.6))
print(mnozenie_2((2.8,), (5.6,)))  # błąd typu

print(dzielenie(2, 0))  # dzielenie przez 0
print(dzielenie("a", "b"))
