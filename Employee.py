class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Name: {self.first_name}, {self.last_name}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\n" \
               f"Address: {self.street}, {self.zip_code}, {self.city}\nPhone: {self.phone}"