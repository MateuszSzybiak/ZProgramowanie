class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"Name: {self.name}\nMarks: {self.marks} "
