from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print('Tu', self.gatunek, 'lece z szybkoscia', self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydajOdglos(self):
        print("piiiiiiiiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Ja sobie będę dziobać!")

    def wydajOdglos(self):
        print("kokokokok")


# ptak1 = Ptak("orzeł", 3)
# ptak2 = Ptak("kura", 0)
# ptak1.latam()
# ptak2.latam()
orz1 = Orzel("orzel", 9)
orz1.latam()
orz1.poluj()
orz1.wydajOdglos()
kur1 = Kura("kura")
kur1.latam()
kur1.dziobanie()
kur1.wydajOdglos()
