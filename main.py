# Mateusz Szybiak 26.10.2021 Lab4

from Library import *
from Student import *
from Book import *
from Property import *

# Zadanie 1


Student1 = Student("Marek", 75)
Student2 = Student("Jerzy", 30)

print(Student2.is_passed())


# Zadanie 2

lib1 = Library('Katowice', 'Wolna 8', '41-100', '8-16', '123456789')

lib2 = Library('Zabrze', 'Meczowa 8', '43-204', '9-16', '987654321')

book1 = Book(lib1, '10/10/2021', 'James', 'Rover', 350)

book2 = Book(lib1, '15/10/2018', 'Michael', 'Jams', 265)

book3 = Book(lib2, '10/06/2013', 'Jim', 'Boyer', 223)

book4 = Book(lib2, '03/11/2015', 'Org', 'Hitt', 260)

book5 = Book(lib2, '09/01/2000', 'Lytt', 'Tyn', 321)

print(book1.__str__())

# Zadanie 3

house = House(150, 5, 600000, "Katowice", 400)
flat = Flat(74, 3, 400000, "Gliwice", 3)
print(house)
print(flat)
