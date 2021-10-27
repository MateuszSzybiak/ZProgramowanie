class Order:
    def __init__(self, employee, student, books, order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"Employee:\n[\n{self.employee}\n]\nStudent:\n[\n{self.student}\n]\n" \
               f"Books:\n[\n{self.books}\n]\nOrder date: {self.order_date}"
