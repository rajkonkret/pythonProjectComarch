class Dom:
    """
    To jest klasa Dom
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.__ilosc_okien = ilosc_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.kolor = wybor
        print("Teraz mamy kolor", self.kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = input("Podaj ilosc okien")
        self.__ilosc_okien = wybor
        print("Teraz mamy okien", self.__ilosc_okien)

    def __farba(self):
        print("Skonczyla sie farba")


dom1 = Dom(100, "czerwony", 6)
dom1.zmien_metraz()
dom1.metraz = "Radek"
dom1.zmien_kolor()
