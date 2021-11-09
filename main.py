class Produkt:
    def __init__(self, cena: float, wymiary: str, rodzaj: str, opis: str, producent: str):
        self._cena = cena
        self._wymiary = wymiary
        self._rodzaj = rodzaj
        self._opis = opis
        self._producent = producent

    @property
    def cena(self):
        return self._cena
    @property
    def wymiary(self):
        return self._wymiary
    @property
    def rodzaj(self):
        return self._rodzaj
    @property
    def opis(self):
        return self._opis
    @property
    def producent(self):
        return self._producent

    def __str__(self) -> str:
        return f"Producent: {self._producent}\n" \
               f"Rodzaj: {self._rodzaj}" \
               f"Wymiary: {self._wymiary}" \
               f"Cena: {self._cena}\n" \
               f"Opis: {self._wymiary}"

class Zamowienie():
    @property
    def nazwyProduktow(self):
        return self._nazwyProduktow

    @property
    def produkty(self):
        return self._produkty

    @property
    def magazyn(self):
        return self._magazyn

    # zwrócenie adresu klienta
    @property
    def adres(self):
        return self._adres

    @property
    def dataDostawy(self):
        return self._dataDostawy

    @nazwyProduktow.setter
    def nazwyProduktow(self, nazwyProduktow: list):
        self._nazwyProduktow = nazwyProduktow

    @produkty.setter
    def produkty(self, produkty: dict):
        self._produkty = produkty


    @adres.setter
    def adres(self, adres):
        self._adres = adres

    @dataDostawy.setter
    def dataDostawy(self, dataDostawy: str):
        self._dataDostawy = dataDostawy

    @magazyn.setter
    def magazyn(self, magazyn: str):
        self._magazyn = magazyn


    # Metoda wyliczająca wartość zamówienia, wykorzystuje słownik postaci:
    # {Nazwa Produktu: [ilość sztuk, cena za sztukę]}

    def wartoscZamowienia(self):
        wartosc = 0
        for i in self._nazwyProduktow:
            wartosc += self._produkty[i][0] * self._produkty[i][1]
        return round(wartosc, 2)


    def __str__(self) -> str:
        return f"Produkty: {self._produkty}\n" \
               f"Data dostawy: {self._dataDostawy}\n" \
               f"Adres: {self._adres}\n" \
               f"Magazyn: {self._magazyn}"

class Magazyn:
    def __init__(self, ulica: str, miasto: str, kod: str, manager: str, liczbaPracownikow: int):
        self._ulica = ulica
        self._miasto = miasto
        self._kod = kod
        self._manager = manager
        self._liczbaPracownikow = liczbaPracownikow

    @property
    def ulica(self):
        return self._ulica

    @property
    def miasto(self):
        return self._miasto

    @property
    def kod(self):
        return self._kod

    @property
    def manager(self):
        return self._manager

    @property
    def liczbaPracownikow(self):
        return self._liczbaPracownikow

    def __str__(self) -> str:
        return f"Manager: {self._manager}\n" \
               f"Ulica: {self._ulica}" \
               f"Miasto: {self._miasto}" \
               f"Kod magazynu: {self._kod}\n" \
               f"Liczba pracowników: {self._liczbaPracownikow}"


class KlientDetaliczny:
    def __init__(self, id: int, imie: str, nazwisko: str, adres: str, historiaZamowien: dict):
        self._id = id
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres = adres
        self._historiaZamowien = historiaZamowien

    @property
    def id(self):
        return self._id

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def adres(self):
        return self._adres

    @property
    def historiaZamowien(self):
        return self.historiaZamowien

    def __str__(self) -> str:
        return f"ID: {self._id}\n" \
               f"Imię: {self._imie}\n" \
               f"Nazwisko: {self._nazwisko}\n" \
               f"Adres: {self._adres}\n" \
               f"historia zamówień: {self._historiaZamowien}"

class KlientBiznesowy:
    def __init__(self, id: int, nazwa, siedziba: str, nip: 'str', historiaZamowien: dict):
        self._id = id
        self._nazwa = nazwa
        self._siedziba = siedziba
        self._nip = nip
        self._historiaZamowien = historiaZamowien

    @property
    def id(self):
        return self._id

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def siedziba(self):
        return self._siedziba

    @property
    def nip(self):
        return self._nip

    @property
    def historiaZamowien(self):
        return self._historiaZamowien

    def __str__(self) -> str:
        return f"ID: {self._id}\n" \
               f"Nazwa firmy: {self._nazwa}\n" \
               f"Siedziba: {self._siedziba}\n" \
               f"NIP: {self._nip}\n" \
               f"historia zamówień: {self._historiaZamowien}"







