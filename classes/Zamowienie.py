from classes.Pacjent import Patient


class Order:
    _order_id: str
    _diets: list  # of diets in the order
    _patient: Patient
    _status: str

    def __init__(self):
        pass

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: str):
        self._order_id = order_id

    @property
    def diets(self):
        return self._diets

    @diets.setter
    def diets(self, diets: list):
        self._diets = diets

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient: Patient):
        self._patient = patient

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    def order_price(self):
        value = 0.0
        for i in self._diets:
            value += i.cost
        return round(value, 2)

    def calories_sum(self):
        summary = 0
        for i in self._diets:
            summary += i.calories
        return summary

    def __str__(self) -> str:
        return f"Order ID: {self._order_id}\n" \
               f"Selected diets: {[{i.name: i.type_of_diet} for i in self._diets]}\n" \
               f"Patient: {self._patient.name} {self._patient.last_name}\n" \
               f"Status: {self._status}\n"
