class Patient:
    def __init__(self, name: str, last_name: str, address: str, age: int):
        self._name = name
        self._last_name = last_name
        self._address = address
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def address(self):
        return self._address

    @property
    def age(self):
        return self._age

    def __str__(self) -> str:
        return f"Name: {self._name}\n" \
               f"Last name: {self._last_name}\n" \
               f"Address: {self._address}\n" \
               f"Age: {self._age}\n"
