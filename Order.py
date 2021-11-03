class Order:
    def __init__(self, employee: str, student: str, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Employee: {self.employee}\nStudent: {self.student}\n" \
               f"Books: {self.books}\nOrder date: {self.order_date}"
