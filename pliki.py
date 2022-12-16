# # print(open.__doc__)  # odczytanie dokumentacji dla funkcji
# print(print.__doc__)
# imie = "Radek"
# print(imie) .py

# w - zeruje plik i pozwala zapaisywac
# a - otwiera plik do zapisu  bez zerowania i dopisuje na końcu pliku
# r - otwiera plik do odczytu - nic nie zapiszemy

with open('test.log', 'w', encoding='utf-8') as f:
    f.write('powitanie\n')
    f.write('jeszcze jedno\n')
    f.write('Witaj świecie\n')

with open('test.log', 'a', encoding='utf-8') as fs:
    fs.write("Dodane")

with open('test.log', 'r', encoding='utf-8') as file_s:
    lines = file_s.read()
    print(lines)

with open('test.log', 'r') as f:
    lines = f.read()
    print(lines)
