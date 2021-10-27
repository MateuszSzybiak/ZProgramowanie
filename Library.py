class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Address of library: {self.street}, {self.zip_code}, {self.city} \nOpening hours: {self.open_hours} \n" \
               f"Phone: {self.phone}"