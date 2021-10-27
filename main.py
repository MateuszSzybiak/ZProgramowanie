#Mateusz Szybiak 26.10.2021 Lab4

from Library import Library
from Student import Student
from Order import Order
from Employee import Employee
from Book import Book
from Property import *

#Zadanie 1


Student1 = Student("Marek", 75)
Student2 = Student("Jerzy", 30)

print(Student2.is_passed())


#Zadanie 2


lib1 = Library('Katowice', 'Wolna 8', '41-100', '8-16', '123456789')

lib2 = Library('Zabrze', 'Meczowa 8', '43-204', '9-16', '987654321')

book1 = Book(lib1, '10/10/2021', 'James', 'Rover', 350)

book2 = Book(lib1, '15/10/2018', 'Michael', 'Jams', 265)

book3 = Book(lib2, '10/06/2013', 'Jim', 'Boyer', 223)

book4 = Book(lib2, '03/11/2015', 'Org', 'Hitt', 260)

book5 = Book(lib2, '09/01/2000', 'Lytt', 'Tyn', 321)

employee1 = Employee('Daniel', 'Skrob', '10/10/2018', '05/01/1988', 'Katowice', 'Nowacka 8', '43-110', '123112332')

employee2 = Employee('Jerzy', 'Góral', '03/12/2016', '01/08/1978', 'Jaworzno', 'Solanki 1', '41-222', '666555444')

employee3 = Employee('Adam', 'Dolny', '17/11/2018', '21/03/1998', 'Sosnowiec', 'Wodna 15', '41-200', '999776431')

student1 = Student("Marek", 75)

student2 = Student("Jerzy", 30)

student3 = Student("Andrzej", 85)

order1 = Order(employee1, student1, book1, '25/10/2021')

order2 = Order(employee3, student2, [book2, book3], '24/10/2021')

print(order1)
print(' ')
print(order2)


#Zadanie 3

house = House(300, 4, 400000, 'Wioskowa 8, Gliwice', 100)

flat = Flat(60, 3, 200000, 'Gwiazdowa 8, Katowice', 3)

print(house)
print(' ')
print(flat)



