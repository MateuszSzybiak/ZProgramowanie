class Property:
    def __init__(self, area, rooms, price, address):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self):
        return f"Property area: {self._area}\nPrice: {self._price}$\nNumber of rooms: {self._rooms}\n" \
               f"Address: {self._address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self):
        return f"House's plot: {self._plot} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self):
        return f"Flat's floor: {self._floor}\nNumber of rooms: {self._rooms}."
