class Dietician:
    def __init__(self, name: str, last_name: str, level_of_education: str, employment_time: str):
        self._name = name
        self._last_name = last_name
        self._level_of_education = level_of_education
        self._employment_time = employment_time

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def level_of_education(self):
        return self._level_of_education

    @property
    def employment_time(self):
        return self._employment_time

    def __str__(self) -> str:
        return f"Name: {self._name}\n" \
               f"Last name: {self._last_name}\n" \
               f"Level of education: {self._level_of_education}\n" \
               f"Employment time: {self._employment_time}\n"
