class Dom:
    """
    To jest klasa Dom
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.metraz = metraz
        self.kolor = kolor
        self.ilosc_okien = ilosc_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.metraz = wybor
        print("Metraz wynosi", self.metraz)

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.kolor = wybor
        print("Teraz mamy kolor", self.kolor)

    def zmien_okna(self):
        wybor = input("Podaj ilosc okien")
        self.ilosc_okien = wybor
        print("Teraz mamy okien", self.ilosc_okien)


dom1 = Dom(23, "zielony", 5)
print(dom1.metraz)
dom1.metraz = 88

dom1.zmien_metraz()
dom1.zmien_kolor()
dom1.zmien_okna()
13:50