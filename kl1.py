# PEP8

class Human:
    """
    To jest klasa Human opisujaca człowieka
    """
    imie = ""
    wiek = None
    plec = ""

    def powitanie(self):
        """
        Metoda w klasie Human
        :return: print z imieniem
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        elif self.plec == 'm':
            print("Ruszyłem w droge")
        else:
            print("Ruszołobym w droge")


print(Human.__doc__)  # wyswietlenie opisu klasy. dokumentacja
czlowiek1 = Human()
print(czlowiek1)
print(czlowiek1.imie)
czlowiek1.powitanie()
print(czlowiek1.wiek)

czlowiek1.imie = "Radek"
print(czlowiek1.imie)
czlowiek1.wiek = 39
print(czlowiek1.wiek)

czlowiek1.powitanie()
czlowiek1.ruszaj()
czl2 = Human()
czl2.plec = 'k'
czl2.ruszaj()
