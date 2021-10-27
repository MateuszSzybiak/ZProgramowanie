class Property:
    def __init__(self, area, rooms: int, price, address) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Area of property: {self.area}\nNumber of rooms: {self.rooms}\nPrice: {self.price}\n" \
               f"Address: {self.address}"

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"House plot: {self.plot} m2"

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"Flat is on {self.floor} floor"



