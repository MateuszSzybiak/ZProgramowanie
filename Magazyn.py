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
