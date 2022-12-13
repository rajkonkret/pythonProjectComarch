lista = []
lang = input("Wpisz znany Ci język programowania")

# Wcięcia obowiązkowe
match lang.lower():  # Java => java
    case "python":  # lang == 'python'
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "c#":
        lista.append(lang)
    case _:
        print("nie ma takiego języka")  # else

print(lista)
