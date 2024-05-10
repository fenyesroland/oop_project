import datetime
from Foglalas import Foglalas
from EgyagyasSzoba import EgyagyasSzoba
from KetagyasSzoba import KetagyasSzoba

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def __str__(self):
        return f"{self.nev} Szálloda\nSzobák:\n" + "\n".join(str(szoba) for szoba in self.szobak)

    def szoba_foglalasa(self, datum, agyak_szama):
        if datum <= datetime.date.today():
            return "Érvénytelen dátum, csak jövőbeli foglalásokat lehet felvenni."

        for szoba in self.szobak:
            if isinstance(szoba, EgyagyasSzoba) and agyak_szama == 1:
                if all(foglalas.datum != datum or foglalas.szoba != szoba for foglalas in self.foglalasok):
                    self.foglalasok.append(Foglalas(szoba, datum))
                    return f"Foglalás sikeresen felvéve: {szoba} - {datum}"
            elif isinstance(szoba, KetagyasSzoba) and agyak_szama == 2:
                if all(foglalas.datum != datum or foglalas.szoba != szoba for foglalas in self.foglalasok):
                    self.foglalasok.append(Foglalas(szoba, datum))
                    return f"Foglalás sikeresen felvéve: {szoba} - {datum}"
        return "Sajnos minden szoba foglalt ezen a napon."

    def foglalas_lemondasa(self, datum, szobaszam):
        for foglalas in self.foglalasok:
            if foglalas.datum == datum and foglalas.szoba.szobaszam == szobaszam:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás sikeresen lemondva: {foglalas}")
                return
        print(f"Nem található foglalás ezen a napon ({datum}) a {szobaszam} szobára.")

    def lista_foglalasok(self):
        for foglalas in self.foglalasok:
            print(foglalas)

