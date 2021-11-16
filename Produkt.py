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
