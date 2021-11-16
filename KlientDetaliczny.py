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
