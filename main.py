# Mateusz Szybiak Informatyka lab2 19.10.2021

from math import *

# Zadanie 2
# a
def names(name) -> None:
    for n in name:
        print(n)


names(['ala', 'kamil', 'darek', 'julia', 'michał'])


# b

def multiply(numbers):
    res = []
    for n in numbers:
        res.append(2 * n)
    return res


def multiply_list(numbers):
    return [2 * j for j in numbers]


print("Sposób 1")
print("Pierwotna lista: {} \nZwrócona lista: {}"
      .format([1, 3, 7, 22, 30], multiply([1, 3, 7, 22, 30])))
print("Sposób 2")
print("Pierwotna lista: {} \nZwrócona lista: {}"
      .format([1, 3, 7, 22, 30], multiply_list([1, 3, 7, 22, 30])))

# c

lista = [1, 2, 5, 10, 13, 14, 18, 21, 24, 30]

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i])


# d

lista1 = [1, 2, 5, 10, 13, 14, 18, 21, 24, 30]

for i in range(floor(len(lista1) / 2)):
    print(lista1[2 * i + 1])

