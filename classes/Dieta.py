class Diet:
    def __init__(self, name: str, calories: int, type_of_diet: str, cost: float):
        self._name = name
        self._calories = calories
        self._type_of_diet = type_of_diet
        self._cost = cost

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    # Regular, vegetarian or vegan
    @property
    def type_of_diet(self):
        return self._type_of_diet

    @property
    def cost(self):
        return self._cost

    def __str__(self) -> str:
        return f"Name: {self._name}\n" \
               f"Calories: {self._calories}\n" \
               f"Type of diet: {self._type_of_diet}\n" \
               f"Cost: {self._cost}\n"
