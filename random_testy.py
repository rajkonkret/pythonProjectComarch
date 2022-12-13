import random

print(random.randint(1, 6))
print(random.random() * 10)

lista = [5, 7, 9, 34, 55, 0]
print(random.choice(lista))

lista2 = list(range(1, 50))
print(lista2)

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
print(lista2)
