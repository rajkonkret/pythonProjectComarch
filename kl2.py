class Human:
    """
    Klasa Human opisujaca czlowieka
    """

    def __init__(self, imie, wiek=0, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

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


czl1 = Human("Radek")
print(czl1.imie)
czl1.powitanie()
czl1.plec = 'm'
print(Human.__doc__)

czl2 = Human("Zenobia")
czl2.wiek = 24
print(czl2.wiek)
print(czl2.imie)
