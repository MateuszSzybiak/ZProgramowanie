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
