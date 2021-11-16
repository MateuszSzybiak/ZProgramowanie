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
